from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import HuggingFaceHub
from langchain_core.runnables import RunnablePassthrough
from retriever.vectorstore import get_vectorstore
import os
from dotenv import load_dotenv
load_dotenv()

def get_spec_chain():
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever()

    prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant that converts high-level business requirements into low-level specs.

Requirement:
{context}

Return:
- Modules
- Database Schema (tables + fields)
- Pseudocode (main functions)

Output in YAML format.
    """)

    llm = HuggingFaceHub(
        # repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        repo_id="google/flan-t5-base",
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
        model_kwargs={"temperature": 0.5, "max_new_tokens": 512},
    )

    chain = (
        {"context": retriever | RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain
