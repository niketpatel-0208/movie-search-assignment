# Movie Semantic Search Assignment

This is my solution for the semantic search on movie plots assignment. I implemented a semantic search engine using SentenceTransformers (all-MiniLM-L6-v2) to find movies based on plot descriptions using natural language queries.

## Prerequisites

- Python 3.8+ (tested with Python 3.8-3.12)
- Git (for cloning the repository)

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/niketpatel-0208/movie-search-assignment.git
   ```

2. **Navigate to the project:**
   ```bash
   cd movie-search-assignment/Assignment-1
   ```

3. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   ```
   
   **Activate it:**
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run Jupyter notebook:**
   ```bash
   jupyter notebook movie_search_solution.ipynb
   ```

*Keep the virtual environment activated for all subsequent commands.*

## Testing

Run the unit tests to verify everything works correctly:

```bash
python -m unittest tests/test_movie_search.py -v
```

**Expected output:**
```
test_search_movies_output_format ... ok
test_search_movies_relevance ... ok  
test_search_movies_similarity_range ... ok
test_search_movies_top_n ... ok

----------------------------------------------------------------------
Ran 4 tests in X.XXXs

OK
```

All 4 tests should pass:
- Output format verification
- Top_n parameter functionality  
- Similarity score range (0-1)
- Semantic relevance of results

*Note: Make sure your virtual environment is activated before running tests.*

## Usage

The `search_movies()` function allows you to search for movies using natural language queries. Here's how to use it:

### Function Signature
```python
search_movies(query, top_n=5)
```

**Parameters:**
- `query` (str): Natural language description of the movie you're looking for
- `top_n` (int, optional): Number of results to return (default: 5)

**Returns:**
- `pandas.DataFrame`: Results with columns `['title', 'plot', 'similarity']`

### Basic Usage

1. **Start Python in your activated virtual environment:**
   ```bash
   python
   ```

2. **Import and use the function:**
   ```python
   from movie_search import search_movies

   # Search for spy thrillers
   result = search_movies('spy thriller in Paris')
   print(result)
   ```

3. **Expected output:**
   ```
              title                                               plot  similarity
   0         Spy Movie  A spy navigates intrigue in Paris to stop a te...    0.769684
   1  Romance in Paris  A couple falls in love in Paris under romantic...    0.388030
   2      Action Flick  A high-octane chase through New York with expl...    0.256777
   ```

### Advanced Usage Examples

**Limit number of results:**
```python
# Get only top 2 results
result = search_movies('spy thriller in Paris', top_n=2)
print(f"Found {len(result)} movies")
print(result)
```

**Different types of queries:**
```python
# Romance movies
romance_results = search_movies('romantic love story')
print("Romance movies:")
print(romance_results[['title', 'similarity']])

# Action movies
action_results = search_movies('action adventure with explosions')
print("\nAction movies:")
print(action_results[['title', 'similarity']])

# Location-based search
paris_results = search_movies('movie set in Paris')
print("\nParis movies:")
print(paris_results[['title', 'similarity']])
```

**Working with results:**
```python
result = search_movies('spy thriller in Paris', top_n=3)

# Get the best match
best_match = result.iloc[0]
print(f"Best match: {best_match['title']} (similarity: {best_match['similarity']:.4f})")

# Filter by similarity threshold
high_similarity = result[result['similarity'] > 0.5]
print(f"High similarity matches: {len(high_similarity)}")
```

### Quick Test Command
For a quick test without entering Python interactive mode:
```bash
python -c "from movie_search import search_movies; print(search_movies('spy thriller in Paris', top_n=2))"
```

The function returns a pandas DataFrame with columns: `title`, `plot`, and `similarity` (sorted by similarity score).

## Cleanup

When you're done working with the project:

1. **Stop Jupyter Notebook (if running):**
   - In the terminal where Jupyter is running: Press `Ctrl+C` twice
   - Or close the browser tab and use `Ctrl+C` in terminal

2. **Exit Python interactive mode (if in Python shell):**
   ```bash
   exit()
   ```

3. **Deactivate virtual environment:**
   ```bash
   deactivate
   ```

### Restarting Later

You can reactivate the environment anytime with:

**Activate virtual environment:**
```bash
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows
```

**Start Jupyter again:**
```bash
jupyter notebook movie_search_solution.ipynb
```
