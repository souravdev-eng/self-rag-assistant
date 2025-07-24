import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from uuid import uuid4

load_dotenv()

# 1. Read the PDF file
loader = PyPDFLoader("./data/NEW_SOURAV_RESUMEA.pdf")
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
