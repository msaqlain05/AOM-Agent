import os
import chromadb
from chromadb.config import Settings


# ------------------------------------------------------------------
# 1. ENV VARS (still one file, but no hard-coding in logic)
# ------------------------------------------------------------------
# Set these once in your shell OR temporarily here for local demo
# os.environ["CHROMA_API_KEY"] = "ck-FkyM2e7bFJ6oa7u6wETpEWQJeZ9x4W1M2pVwRPLVrb2r"
# os.environ["CHROMA_TENANT"] = "79116575-97d2-4906-80ad-617c570abbda"
# os.environ["CHROMA_DATABASE"] = "DEV"

client = chromadb.CloudClient(
  api_key='ck-FkyM2e7bFJ6oa7u6wETpEWQJeZ9x4W1M2pVwRPLVrb2r',
  tenant='79116575-97d2-4906-80ad-617c570abbda',
  database='DEV'
)


collection = client.get_or_create_collection("demo_collection")
print(collection.count())
# collection.add(
#     ids=["id1", "id2", "id3"],
#     documents=[
#         "Pineapple grows in tropical climates",
#         "Oranges are citrus fruits",
#         "Hawaii is a tropical location"
#     ],
#     embeddings=[
#         [0.10, 0.20, 0.30],
#         [0.90, 0.80, 0.70],
#         [0.12, 0.22, 0.32]
#     ]
# )

# print("✅ Data stored in Chroma Cloud")



results = collection.query(
    query_embeddings=[[0.10, 0.20, 0.30]],
    n_results=2
)

print("IDs:", results["ids"])
print("Documents:", results["documents"])
print("Distances:", results["distances"])
print(results)