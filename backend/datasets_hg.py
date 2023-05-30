from datasets import load_dataset

#downloading at once
def download_data(path = "Cohere/wikipedia-22-12-simple-embeddings"):
    """
    Downloads data from hugging face.
    """
    docs = load_dataset(f"{path}", split="train")
    return docs