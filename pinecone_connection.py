import os
from dotenv import load_dotenv
from pinecone import ServerlessSpec, Pinecone


load_dotenv()

index_name = os.getenv("PINECONE_INDEX_NAME")


def connect_to_pinecone():
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"), environment="us-east-1")
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )
        print(f"Index {index_name} created")
    else:
        print(f"Index {index_name} already exists")
    return pc
