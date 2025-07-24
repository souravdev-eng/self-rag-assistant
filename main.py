import os
from dotenv import load_dotenv
from pinecone_connection import connect_to_pinecone
from graph.ingest_node import ingest_node

load_dotenv()

if __name__ == "__main__":
    connect_to_pinecone()
    ingest_node()
