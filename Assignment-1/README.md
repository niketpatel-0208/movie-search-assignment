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

**Actual test output:**
    test_search_movies_output_format (tests.test_movie_search.TestMovieSearch.test_search_movies_output_format)
    Test if search_movies returns a DataFrame with correct columns. ... ok
    test_search_movies_relevance (tests.test_movie_search.TestMovieSearch.test_search_movies_relevance)
    Test if returned movies are relevant to the query. ... ok
    test_search_movies_similarity_range (tests.test_movie_search.TestMovieSearch.test_search_movies_similarity_range)
    Test if similarity scores are between 0 and 1. ... ok
    test_search_movies_top_n (tests.test_movie_search.TestMovieSearch.test_search_movies_top_n)
    Test if search_movies returns the correct number of results. ... ok

    ----------------------------------------------------------------------
    Ran 4 tests in 3.781s

    OK

All 4 tests should pass:
- Output format verification
- Top_n parameter functionality  
- Similarity score range (0-1)
- Semantic relevance of results

*Note: Make sure your virtual environment is activated before running tests.*

## Usage

The `search_movies()` function allows you to search for movies using natural language queries.

### Function Signature
    search_movies(query, top_n=5)

**Parameters:**
- `query` (str): Natural language description of the movie you're looking for  
- `top_n` (int, optional): Number of results to return (default: 5)

**Returns:**
- `pandas.DataFrame`: Results with columns `['title', 'plot', 'similarity']`

### Quick Test
```bash
python -c "from movie_search import search_movies; print(search_movies('spy thriller in Paris', top_n=2))"
```

**Output:**
                  title                                               plot  similarity
    0         Spy Movie  A spy navigates intrigue in Paris to stop a te...    0.769684
    1  Romance in Paris  A couple falls in love in Paris under romantic...    0.388030

### Comprehensive Examples

For detailed usage examples, run the provided examples file:

```bash
python usage_examples.py
```

This will demonstrate:
- Basic movie searching
- Working with different query types  
- Filtering results by similarity
- Advanced result manipulation

**Sample output from usage examples:**
    ============================================================
    Movie Semantic Search - Usage Examples
    ============================================================

    1. Basic Search - 'spy thriller in Paris'
    ----------------------------------------
                  title                                               plot  similarity
    0         Spy Movie  A spy navigates intrigue in Paris to stop a te...    0.769684
    1  Romance in Paris  A couple falls in love in Paris under romantic...    0.388030
    2      Action Flick  A high-octane chase through New York with expl...    0.256777

    2. Limited Results - top 2 movies
    ----------------------------------------
                  title                                               plot  similarity
    0         Spy Movie  A spy navigates intrigue in Paris to stop a te...    0.769684
    1  Romance in Paris  A couple falls in love in Paris under romantic...    0.388030

    3. Romance Movies
    ----------------------------------------
                  title  similarity
    0  Romance in Paris    0.553853
    1      Action Flick    0.143565

    4. Action Movies
    ----------------------------------------
              title  similarity
    0  Action Flick    0.544479
    1     Spy Movie    0.212702

    5. Working with Results
    ----------------------------------------
    Best match: Spy Movie (similarity: 0.7697)
    High similarity matches: 1 movies
           title  similarity
    0  Spy Movie    0.769684

    ============================================================
    Usage examples completed!
    ============================================================

The function returns a pandas DataFrame with columns: `title`, `plot`, and `similarity` (sorted by similarity score).

## Cleanup

When you're done working with the project:

1. **Stop Jupyter Notebook (if running):**
   - In the terminal where Jupyter is running: Press `Ctrl+C` twice
   - Or close the browser tab and use `Ctrl+C` in terminal


2. **Deactivate virtual environment:**
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
