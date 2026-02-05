from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings


# load function

def load_pdf_file(data):
    loader = DirectoryLoader(data,
                            glob = "*.pdf",
                            loader_cls = PyPDFLoader)

    documents = loader.load()
    return documents


# split function

def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500 , chunk_overlap=20)
    text_chunk = text_splitter.split_documents(extracted_data)
    return text_chunk

# download function 

from langchain_community.embeddings import HuggingFaceEmbeddings
def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings( model_name = "sentence-transformers/all-MiniLM-L6-v2")
    return embeddings

