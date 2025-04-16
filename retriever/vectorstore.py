from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import JSONLoader
import os

VECTORSTORE_PATH = "data/faiss_index"

def get_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # ✅ Load from disk if already built
    if os.path.exists(VECTORSTORE_PATH):
        return FAISS.load_local(VECTORSTORE_PATH, embeddings, allow_dangerous_deserialization=True)

    # 🚧 First-time setup: Load and create the vectorstore
    loader = JSONLoader(
        file_path="data/examples.jsonl",
        jq_schema=".text",
        json_lines=True)
    docs = loader.load()

    vectorstore = FAISS.from_documents(docs, embeddings)

    # 💾 Save to disk for future use
    vectorstore.save_local(VECTORSTORE_PATH)

    return vectorstore
