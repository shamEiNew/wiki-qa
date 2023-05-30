import os

#Cohere client key for embeddings
COHERE_CLIENT_KEY = os.environ["COHERE_KEY"]

#Pinecone vector db for storing embeddings
PINECONE_KEY = os.environ["PINECONE_KEY"]
PINECONE_ENV = os.environ["PINECONE_ENV"]

#openai key for model api
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]