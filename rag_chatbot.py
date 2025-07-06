from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI

import os
from dotenv import load_dotenv

load_dotenv()

def create_qa_chain(document_text):
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len
    )
    documents = splitter.create_documents([document_text])

    embeddings = HuggingFaceEmbeddings()

    vectorstore = FAISS.from_documents(documents, embeddings)

    retriever = vectorstore.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0),
        chain_type="stuff",
        retriever=retriever
    )

    return qa_chain
