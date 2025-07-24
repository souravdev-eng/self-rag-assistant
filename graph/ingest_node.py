import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from uuid import uuid4

load_dotenv()


def ingest_node():
    file_path = os.getenv("FILE_PATH")
    # 1. Read the PDF file
    if file_path:
        loader = PyPDFLoader(file_path)
    else:
        # Use path relative to current file location
        current_dir = os.path.dirname(os.path.abspath(__file__))
        default_path = os.path.join(current_dir, "data", "demo.pdf")
        loader = PyPDFLoader(default_path)
    docs = loader.load()

    # 2. Extract the text from the PDF & Chunk it
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    chunks = text_splitter.split_documents(docs)

    # 3. Embed the chunks
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    # 4. Store the chunks in a vector database
    vector_store = PineconeVectorStore(
        index_name=os.getenv("PINECONE_INDEX_NAME"),
        embedding=embeddings,
    )

    uuids = [str(uuid4()) for _ in range(len(chunks))]
    vector_store.add_documents(documents=chunks, ids=uuids)
