from transformers import pipeline

class RAGAgent:
    def __init__(self, retriever):
        self.retriever = retriever
        self.llm = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf")

    def answer(self, query):
        docs = self.retriever.retrieve(query)
        context = "\n".join([doc[0] for doc in docs])
        prompt = f"Answer the question based on the context below:\n{context}\n\nQuestion: {query}"
        return self.llm(prompt, max_length=300)[0]["generated_text"]
