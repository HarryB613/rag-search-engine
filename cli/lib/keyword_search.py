from .search_utils import DEFAULT_SEARCH_LIMIT, load_movies
import string


def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    results = []
    stripped_query = query.lower().translate(str.maketrans("", "", string.punctuation))
    for movie in movies:
        movie_title = movie["title"].lower().translate(str.maketrans("", "", string.punctuation))
        if stripped_query in movie_title:
            results.append(movie)
            if len(results) >= limit:
                break
    return results