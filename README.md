# Medical Bot

A RAG-based (Retrieval-Augmented Generation) medical chatbot designed to provide accurate answers to medical queries using a curated knowledge base of PDF documents.

## 🚀 Features

-   **Medical Q&A:** Answers user queries specifically related to medical topics found in the knowledge base.
-   **RAG Implementation:** Uses Retrieval-Augmented Generation to ground answers in provided documents, reducing hallucinations.
-   **Vector Search:** Utilizes FAISS (Facebook AI Similarity Search) for efficient similarity search of relevant document chunks.
-   **Local LLM Support:** Integrated with Ollama (Mistral model) for local, privacy-focused inference.
-   **Web Interface:** Simple and intuitive chat interface built with Flask and HTML/CSS.

## 🛠️ Tech Stack

-   **Backend Framework:** Flask
-   **Language:** Python
-   **LLM:** Ollama (Mistral)
-   **Orchestration:** LangChain
-   **Vector Store:** FAISS
-   **Embeddings:** HuggingFace Embeddings (`sentence-transformers/all-MiniLM-L6-v2`)
-   **Frontend:** HTML, CSS

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

1.  **Python 3.8+**
2.  **Ollama**: Download and install from [ollama.com](https://ollama.com/).
    -   Pull the Mistral model:
        ```bash
        ollama pull mistral
        ```

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd medical_bot
    ```

2.  **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables:**
    Create a `.env` file in the root directory if necessary (e.g., for specific API keys, though this project primarily uses local models).

## 🏃 Usage

### 1. Ingest Data (Create Index)
Place your medical PDF documents in the `Data/` directory. Then run the indexing script to process the PDFs and create the FAISS vector store.

```bash
python store_index.py
```
This will create a `faiss_index` folder containing the vector database.

### 2. Run the Application
Start the Flask web server:

```bash
python app.py
```

### 3. Access the Chatbot
Open your web browser and navigate to:
`http://localhost:8000`

## 📂 Project Structure

```
medical_bot/
├── Data/                   # Directory for source PDF documents
├── faiss_index/            # Stored vector index
├── src/
│   ├── helper.py           # Helper functions for loading and splitting data
│   └── prompt.py           # Prompt templates for the LLM
├── static/                 # CSS and static files
├── template/               # HTML templates
├── app.py                  # Main Flask application
├── store_index.py          # Script to ingest data and create index
├── requirements.txt        # Python dependencies
└── setup.py                # Package setup script
```
