import os
from dotenv import load_dotenv
from pinecone_connection import connect_to_pinecone

load_dotenv()

if __name__ == "__main__":
    pc = connect_to_pinecone()
    print(pc.list_indexes())
