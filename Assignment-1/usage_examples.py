"""
Movie Search Usage Examples
============================

This file demonstrates various ways to use the search_movies() function.
Run this file to see the movie search engine in action.

Usage: python usage_examples.py
"""

from movie_search import search_movies
import pandas as pd

def main():
    print("=" * 60)
    print("Movie Semantic Search - Usage Examples")
    print("=" * 60)
    
    # Example 1: Basic search
    print("\n1. Basic Search - 'spy thriller in Paris'")
    print("-" * 40)
    result = search_movies('spy thriller in Paris')
    print(result)
    
    # Example 2: Limited results
    print("\n2. Limited Results - top 2 movies")
    print("-" * 40)
    result = search_movies('spy thriller in Paris', top_n=2)
    print(result)
    
    # Example 3: Different query types
    print("\n3. Romance Movies")
    print("-" * 40)
    romance_results = search_movies('romantic love story', top_n=2)
    print(romance_results[['title', 'similarity']])
    
    print("\n4. Action Movies")
    print("-" * 40)
    action_results = search_movies('action adventure with explosions', top_n=2)
    print(action_results[['title', 'similarity']])
    
    # Example 4: Working with results
    print("\n5. Working with Results")
    print("-" * 40)
    result = search_movies('spy thriller in Paris', top_n=3)
    
    # Get the best match
    best_match = result.iloc[0]
    print(f"Best match: {best_match['title']} (similarity: {best_match['similarity']:.4f})")
    
    # Filter by similarity threshold
    high_similarity = result[result['similarity'] > 0.5]
    print(f"High similarity matches: {len(high_similarity)} movies")
    print(high_similarity[['title', 'similarity']])
    
    print("\n" + "=" * 60)
    print("Usage examples completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()
