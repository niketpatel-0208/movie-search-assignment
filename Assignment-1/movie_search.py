import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load dataset and create embeddings (global for testing)
df = pd.read_csv('movies.csv')

# Load the Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Convert the 'plot' of the movies into embeddings
plot_embeddings = model.encode(df['plot'].tolist(), convert_to_tensor=False)


def search_movies(query, top_n=5):
    """
    Search for movies based on semantic similarity to the query.
    
    Args:
        query (str): The search query describing desired movie characteristics
        top_n (int): Number of top similar movies to return (default: 5)
    
    Returns:
        pd.DataFrame: DataFrame with columns ['title', 'plot', 'similarity']
                     sorted by similarity score in descending order
    """
    # Encode the query using the same model
    query_embedding = model.encode([query], convert_to_tensor=False)
    
    # Calculate cosine similarity between query and all movie plots
    similarities = cosine_similarity(query_embedding, plot_embeddings)[0]
    
    # Get indices of top_n most similar movies
    top_indices = np.argsort(similarities)[::-1][:top_n]
    
    # Create result DataFrame
    result_df = df.iloc[top_indices].copy()
    result_df['similarity'] = similarities[top_indices]
    
    # Reset index for clean output
    result_df = result_df.reset_index(drop=True)
    
    return result_df[['title', 'plot', 'similarity']]