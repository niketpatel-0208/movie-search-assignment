# Movie Semantic Search Assignment

This is my solution for the semantic search on movie plots assignment. I implemented a semantic search engine using SentenceTransformers (all-MiniLM-L6-v2) to find movies based on plot descriptions using natural language queries.

## Prerequisites

- Python 3.8+ (tested with Python 3.8-3.12)
- Git (for cloning the repository)

## Setup

1. Clone: `git clone https://github.com/niketpatel-0208/movie-search-assignment.git`
2. Navigate: `cd movie-search-assignment/Assignment-1`
3. Create virtual environment: `python -m venv venv` and activate it:
   - macOS/Linux: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run notebook: `jupyter notebook movie_search_solution.ipynb`

*Keep the virtual environment activated for all subsequent commands.*

## Testing

Run: `python -m unittest tests/test_movie_search.py -v`

*Note: Make sure your virtual environment is activated before running tests.*

All 4 tests should pass:
- Output format verification
- Top_n parameter functionality  
- Similarity score range (0-1)
- Semantic relevance of results

## Usage

Test the function: `search_movies('spy thriller in Paris')`

Example:
```python
from movie_search import search_movies

# Basic search
result = search_movies('spy thriller in Paris', top_n=3)
print(result)

# Expected output:
#         title                                               plot  similarity
#     Spy Movie  A spy navigates intrigue in Paris to stop a te...    0.769684
# Romance in Paris  A couple falls in love in Paris under romantic...    0.388030
#  Action Flick  A high-octane chase through New York with expl...    0.256777
```

The function returns a pandas DataFrame with columns: `title`, `plot`, and `similarity` (sorted by similarity score).

## Cleanup

When you're done working with the project:

```bash
deactivate  # Exit the virtual environment
```

You can reactivate the environment anytime with:
```bash
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows
```
