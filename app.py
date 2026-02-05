from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings


from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.helper import load_pdf_file , text_split , download_hugging_face_embeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os
from langchain_community.embeddings import HuggingFaceEmbeddings

from typing import List
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from langchain_community.llms import Ollama

from src.prompt import *
import os 

app = Flask(__name__)
embeddings = download_hugging_face_embeddings()
index_name = "faiss-index"

vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# retrieved_docs = retriever.invoke("What is Acne?")

# from langchain_core.prompts import ChatPromptTemplate

# template = ChatPromptTemplate(
#     [
#         ("system", "You are a helpful AI bot. Your name is {name}."),
#         ("human", "Hello, how are you doing?"),
#         ("ai", "I'm doing well, thanks!"),
#         ("human", "{user_input}"),
#     ]
# )

# prompt_value = template.invoke(
#     {
#         "name": "Bob",
#         "user_input": "What is your name?",
#     }
# )

from typing import List
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever

class SimpleRetriever(BaseRetriever):
    docs: List[Document]
    k: int = 5

    def _get_relevant_documents(self, query: str) -> List[Document]:
        return self.docs[: self.k]

    async def _aget_relevant_documents(self, query: str) -> List[Document]:
        return self.docs[: self.k]


docs = [
    Document(page_content="Acne is a common skin condition."),
    Document(page_content="Acne occurs when hair follicles get clogged."),
    Document(page_content="Treatments include medication and skincare."),
]

retriever = SimpleRetriever(docs=docs, k=2)
from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI bot. Your name is {name}."),
        ("system", "Use the following context to answer:\n{context}"),
        ("human", "{user_input}"),
    ]
)

# 1. Get relevant documents
query = "What is acne?"
retrieved_docs = retriever.invoke(query)

# 2. Convert docs to context string
context = "\n".join(doc.page_content for doc in retrieved_docs)

# 3. Create prompt value
prompt_value = template.invoke(
    {
        "name": "Bob",
        "user_input": query,
        "context": context,
    }
)


llm = Ollama(
    model="mistral",
    temperature=0.4
)
# question_answer_chain = create_stuff_documents_chain(llm, template)
# rag_chain = create_retrieval_chain(retriever, question_answer_chain)
response = llm.invoke(prompt_value)
print(response)


@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get" , methods=["GET" , "POST"])
def chat():
    msg = request.form["msg"]
    input = msg 
    print(input)
    response = rag_chain.invoke({"input" :msg})
    print("Response :" , response["answer"])
    return str(response["answer"])


if __name__ == '__main__':
    app.run(host="0.0.0.0" , port = 8000 , debug = True)



