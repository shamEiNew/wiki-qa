import os
import streamlit as st

#Cohere client key for embeddings
COHERE_CLIENT_KEY = st.secrets["COHERE_KEY"]

#Pinecone vector db for storing embeddings
PINECONE_KEY = st.secrets["PINECONE_KEY"]
PINECONE_ENV = st.secrets["PINECONE_ENV"]

#openai key for model api
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]