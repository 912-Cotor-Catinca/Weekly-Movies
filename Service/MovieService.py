"""
Implement the movie service
"""
from Domain.Movie import Movie


class MovieService:
    def __init__(self, movie_repo):
        self._movie_repo = movie_repo

    def get_all_movies(self):
        return self._movie_repo.get_movies()

    def get_movies_by_cinema(self, cinemaid):
        return self._movie_repo.get_movies_by_cinema(cinemaid)

    def get_movies_by_genre(self, genre):
        return self._movie_repo.get_movies_by_genre(genre)
