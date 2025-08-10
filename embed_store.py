from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class EmbedStore:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.chunks = []

    def build(self, chunks):
        embeddings = self.model.encode(chunks, convert_to_numpy=True)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)
        self.chunks = chunks

    def search(self, query, k=3):
        q_embed = self.model.encode([query], convert_to_numpy=True)
        D, I = self.index.search(q_embed, k)
        return [(self.chunks[i], float(D[0][j])) for j, i in enumerate(I[0])]
