import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset and create embeddings (global for testing)
df = pd.read_csv('movies.csv')
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(df['plot'].tolist(), convert_to_tensor=False)

def search_movies(query, top_n=5):
    query_emb = model.encode([query], convert_to_tensor=False)
    sims = cosine_similarity(query_emb, embeddings)[0]
    top_idx = sims.argsort()[::-1][:top_n]
    results = df.iloc[top_idx][['title', 'plot']].copy()
    results['similarity'] = sims[top_idx]
    return results