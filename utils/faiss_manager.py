import faiss
import numpy as np

class FAISSManager:
    def __init__(self, dimension=384):
        self.index = faiss.IndexFlatL2(dimension)

    def add_embeddings(self, embeddings):
        vectors = np.array(embeddings).astype('float32')
        self.index.add(vectors)

    def search(self, query_vector, top_k=5):
        query_vector = np.array([query_vector]).astype('float32')
        distances, indices = self.index.search(query_vector, top_k)
        return distances[0], indices[0]
