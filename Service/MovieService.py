"""
Implement the movie service
"""
from Domain.Movie import Movie


class MovieService:
    def __init__(self, movie_repo):
        self._movie_repo = movie_repo

    def get_all_movies(self):
        return self._movie_repo.get_movies()

    # def __len__(self):
    #     return len(self._movie_repo)
    #
    # def add_movie(self, id_movie, title, director, genre, time, language, location):
    #     """
    #     Instantiates a movie object with a given [id_movie], a[title] and a[director] and adds it to the repo
    #     :param location: movie's location
    #     :param language: movie's language
    #     :param time: movie's time
    #     :param genre: movie's genre
    #     :param id_movie: The movie's id
    #     :param title: movie's title
    #     :param director: movie's author
    #     :return:
    #     """
    #     movie = Movie(id_movie, title, director, genre, time, language, location)
    #     if self.find(movie.movie_id) != -1:
    #         raise ValueError('movie with given id already exist')
    #     else:
    #         self._movie_repo.add(movie)
    #     return movie
    #
    # def update_movie(self, id, title, director):
    #     """
    #     Updates the title and the author of an instance of a movie object with a given id
    #     :param id: movie's id
    #     :param title: updated title
    #     :param director: updated author
    #     :return:
    #     """
    #     for b in self._movie_repo.get_all():
    #         if b.movie_id == id:
    #             old_title = b.title
    #             old_author = b.author
    #     new_movie = self._movie_repo.update(id, title, director)
    #     return new_movie, old_title, old_author
    #
    # def find(self, id):
    #     """
    #     Find by id a movie
    #     :param id: movie's id
    #     :return: the index if there exist or -1 otherwise
    #     """
    #     for i in range(len(self._movie_repo)):
    #         if self._movie_repo[i].movie_id == id:
    #             return i
    #     return -1
    #
    # def delete_movie(self, id):
    #     """
    #     Deletes a movie object with the given [id]
    #     :param id:
    #     :return:
    #     """
    #     movie = self._movie_repo.delete(id)
    #     return movie
    #
    # def display(self):
    #     """
    #     Return a shallow copy of the list of movies
    #     :return: the list of movies
    #     """
    #     return self._movie_repo.get_all()
    #
    # def search_title(self, title):
    #     result = []
    #     for b in self._movie_repo.get_all():
    #         if title.lower() in b.title.lower():
    #             result.append(b)
    #     return result
    #
    # def search_director(self, name):
    #     result = []
    #     for b in self._movie_repo.get_all():
    #         if name.lower() in b.director.lower():
    #             result.append(b)
    #     return result
    #
    # def search_id(self, movie_id):
    #     result = []
    #     for b in self._movie_repo.get_all():
    #         if movie_id.lower() in b.movie_id.lower():
    #             result.append(b)
    #     return result
