import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

def create_index(texts):
    embeddings = embed_model.encode(texts)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))
    return index, embeddings, texts

def search(query, index, texts, embeddings, k=2):
    q_vec = embed_model.encode([query])
    D, I = index.search(np.array(q_vec).astype("float32"), k)
    return " ".join([texts[i] for i in I[0]])
