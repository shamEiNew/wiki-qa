from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

PINECONE_KEY = os.getenv("PINECONE_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
COHERE_CLIENT_KEY = os.getenv("COHERE_KEY")
