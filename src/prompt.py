from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful medical assistant. Use the following context to answer the question:\n{context}"),
        ("human", "{input}"),
    ]
)