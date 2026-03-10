from .search_utils import DEFAULT_SEARCH_LIMIT, load_movies
import string


def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    results = []
    stripped_query = query.lower().translate(str.maketrans("", "", string.punctuation))
    query_words = stripped_query.split()
    for movie in movies:
        movie_title = movie["title"].lower().translate(str.maketrans("", "", string.punctuation))
        movie_title_words = movie_title.split()
        for query_word in query_words:
            for title_word in movie_title_words:
                if query_word in title_word and movie not in results:
                    results.append(movie)
                    if len(results) >= limit:
                        break
    return results