# # creation pinecone vector db
# from pinecone import Pinecone, ServerlessSpec
# from pinecone.core.client.rest import ApiException
# from .secret_keys import *


# def create_pinecone_index(table_name, dimension=768, metric="cosine"):
#     print("Initializing Pinecone (Serverless)...")

#     pc = Pinecone(api_key=PINECONE_KEY)

#     existing_indexes = [idx["name"] for idx in pc.list_indexes()]

#     if table_name not in existing_indexes:
#         print(f"{table_name} not found. Creating serverless index...")

#         pc.create_index(
#             name=table_name,
#             dimension=dimension,
#             metric=metric,
#             spec=ServerlessSpec(
#                 cloud="aws",           # required for serverless
#                 region="us-east-1"     # always allowed on free tier
#             )
#         )

#     else:
#         print(f"{table_name} already exists.")

#     index = pc.Index(table_name)
#     return index



# def upsert_vectors_to_pine(index, docs, vector_space, batch_size, to_start=0):
#     for i in range(to_start, vector_space, batch_size):

#         i_end = min(i + batch_size, vector_space)
#         temp = docs[i:i_end]

#         ids = [str(id) for id in temp["id"]]
#         embeds = temp["emb"]

#         meta = [{
#             "title": article[0],
#             "text": article[1],
#             "url": article[2],
#             "wiki_id": article[3]
#         } for article in zip(temp["title"], temp["text"], temp["url"], temp["wiki_id"])]

#         to_upsert = list(zip(ids, embeds, meta))

#         try:
#             index.upsert(vectors=to_upsert)
#         except ApiException:
#             print("Index limit approached or upsert error occurred.")
#             break



# creation pinecone vector db
from pinecone import Pinecone, ServerlessSpec
from .secret_keys import *


def create_pinecone_index(table_name, dimension=768, metric="cosine"):
    print("Initializing Pinecone (Serverless)...")

    pc = Pinecone(api_key=PINECONE_KEY)

    existing_indexes = [idx["name"] for idx in pc.list_indexes()]

    if table_name not in existing_indexes:
        print(f"{table_name} not found. Creating serverless index...")

        pc.create_index(
            name=table_name,
            dimension=dimension,
            metric=metric,
            spec=ServerlessSpec(
                cloud="aws",           # required for serverless
                region="us-east-1"     # always allowed on free tier
            )
        )

    else:
        print(f"{table_name} already exists.")

    index = pc.Index(table_name)
    return index



def upsert_vectors_to_pine(index, docs, vector_space, batch_size, to_start=0):
    for i in range(to_start, vector_space, batch_size):

        i_end = min(i + batch_size, vector_space)
        temp = docs[i:i_end]

        ids = [str(id) for id in temp["id"]]
        embeds = temp["emb"]

        meta = [{
            "title": article[0],
            "text": article[1],
            "url": article[2],
            "wiki_id": article[3]
        } for article in zip(temp["title"], temp["text"], temp["url"], temp["wiki_id"])]

        to_upsert = list(zip(ids, embeds, meta))

        try:
            index.upsert(vectors=to_upsert)
        except Exception:
            print("Index limit approached or upsert error occurred.")
            break
