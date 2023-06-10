#import libraries
from langchain.vectorstores import Pinecone
from langchain.llms import OpenAI
from langchain.embeddings import CohereEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.chains import LLMChain, SimpleSequentialChain, RetrievalQA
from langchain.prompts import PromptTemplate
from .secret_keys import *
import pinecone

def co_embedding(model = "multilingual-22-12"):
    embeddings = CohereEmbeddings(cohere_api_key=COHERE_CLIENT_KEY,
                                   model = model)
    
    return embeddings
    

# switch back to normal index for langchain
def vectorstores(index, embeddings, text_field="text"):
    vectorstore = Pinecone(index, embeddings.embed_query,text_field)
    return vectorstore

def llm_openai(model_name='gpt-3.5-turbo', temperature=0.0):
    

    # completion llm
    llm = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model_name=model_name,
        temperature=temperature
    )

    return llm

def retrieval_qa(llm,vectorstore):
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )
    return qa

# create the query embedding
def similarity_search(co,index, query, neighbors=5, model='multilingual-22-12'):
  xq = co.embed(
      texts=[query],
      model=model,
      truncate='LEFT',
      ).embeddings
  res = index.query(xq, top_k=neighbors, include_metadata=True)
  for match in res['matches']:
    print(f"{match['score']:.2f}: {match['metadata']['text']}")




