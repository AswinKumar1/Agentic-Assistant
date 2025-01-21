from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

client = QdrantClient("localhost", port=6333)

def store_knowledge(id, vector, payload):
    client.upsert(
        collection_name="knowledge_base",
        points=[PointStruct(id=id, vector=vector, payload=payload)]
    )

def query_knowledge(vector, top_k=1):
    result = client.search(
        collection_name="knowledge_base",
        query_vector=vector,
        limit=top_k
    )
    return result
