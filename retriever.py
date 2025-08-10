from .embed_store import EmbedStore

class Retriever:
    def __init__(self, embed_store):
        self.embed_store = embed_store

    def retrieve(self, query, k=3):
        return self.embed_store.search(query, k)
