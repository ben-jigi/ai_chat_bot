import faiss
import os
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_text(texts):

    embeddings = embedding_model.encode(texts)

    embeddings = np.array(embeddings).astype("float32")

    faiss.normalize_L2(embeddings)

    return embeddings


def create_add_load(chunks, index_path="faiss_index.index", chunks_path="chunks.pkl"):

    if os.path.exists(index_path) and os.path.exists(chunks_path):

        index = faiss.read_index(index_path)

        with open(chunks_path, "rb") as f:
            chunks = pickle.load(f)

        return index, chunks

    if len(chunks) == 0:

        dim = 384
        index = faiss.IndexFlatIP(dim)

        return index, []

    texts = [chunk["text"] for chunk in chunks]

    embeddings = embed_text(texts)

    dim = embeddings.shape[1]

    index = faiss.IndexFlatIP(dim)

    index.add(embeddings)

    faiss.write_index(index, index_path)

    with open(chunks_path, "wb") as f:
        pickle.dump(chunks, f)

    return index, chunks


def query_index(index, query, chunks_list, top_k=5):

    if len(chunks_list) == 0:
        return []

    query_embedding = embed_text([query])

    similarities, indices = index.search(query_embedding, top_k)

    results = []

    for score, idx in zip(similarities[0], indices[0]):

        if idx >= len(chunks_list):
            continue

        chunk = chunks_list[idx]

        results.append({
            "text": chunk["text"],
            "source": chunk["source"],
            "chunk_id": chunk["chunk_id"],
            "score": float(score)
        })

    return results