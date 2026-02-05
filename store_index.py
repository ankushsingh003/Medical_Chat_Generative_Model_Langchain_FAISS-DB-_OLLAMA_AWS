from src.helper import load_pdf_file , text_split , download_hugging_face_embeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os
from langchain_community.embeddings import HuggingFaceEmbeddings


load_dotenv()
extracted_data = load_pdf_file(data='Data/')
text_chunk=text_split(extracted_data)
embeddings=download_hugging_face_embeddings()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(
    documents=text_chunk,
    embedding=embeddings
)
vectorstore.save_local("faiss_index")