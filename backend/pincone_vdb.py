#creation pincone vector db
import pinecone
from pinecone.core.client.rest import ApiException
from .secret_keys import *

    

def create_pinecone_index(table_name, dimension=768, metric="cosine",
                          pod_type="p1"):
    
    print("Initializing Pincone")
    pinecone.init(api_key=PINECONE_KEY,
              environment=PINECONE_ENV)
    if table_name not in pinecone.list_indexes():
        print(f"{table_name} not in Pincone Indexes")
        print(f"Creating index with name {table_name}")
        pinecone.create_index(table_name, dimension=dimension, metric=metric,
                              pod_type=pod_type)
        index = pinecone.Index(table_name)
        
    else:
        print(f"{table_name} already exists in index")
        index = pinecone.Index(table_name)

    return index


def upsert_vectors_to_pine(index, docs, vector_space, batch_size, to_start=0):
  for i in range(to_start, vector_space, batch_size):

  
    i_end = min(i+batch_size,vector_space)
    temp = docs[i:i_end]
    ids = [str(id) for id in temp["id"]]
    embeds =  temp["emb"]
    print("embeds done")
    meta = [{"title":article[0],
            "text":article[1],
            "url":article[2],
            "wiki_id":article[3]} for article in zip(temp["title"],
                                                      temp["text"],
                                                      temp["url"],
                                                      temp["wiki_id"])]
    to_upsert = list(zip(ids, embeds, meta))
    try:
      index.upsert(vectors=to_upsert)
    except ApiException:
      print("index limit approached")
      break
