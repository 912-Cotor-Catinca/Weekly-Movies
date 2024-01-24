from sqlalchemy.orm import Session
from Models.models import MovieModel

from Models.models import MovieModel


class MovieRepo:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_movies(self):
        return self.db_session.query(MovieModel).all()

    # @property
    # def movie_list(self):
    #     return self._movie_list
    #
    # def __len__(self):
    #     return len(self._movie_list)
    #
    # def add(self, movie):
    #     """
    #     Appends a new movie in the client list
    #     :param movie: an instance of the Movie object
    #     :return:
    #     """
    #     if movie in self._movie_list:
    #         raise Exception('The given id already exist')
    #     self._movie_list.append(movie)
    #
    # def delete(self, id):
    #     """
    #     Delete a movie from the list
    #     :param id: an instance of a Movie Object
    #     :return:
    #     """
    #     for movie in self._movie_list:
    #         if movie.movie_id == id:
    #             current = movie
    #             self._movie_list.remove(current)
    #             return current
    #     raise Exception('The given id does not exist')
    #
    # def update(self, id, time):
    #     """
    #     Updates the time attribute of the given [id]
    #     :param id: the instance of a Movie object from the list that is to be updated
    #     :param time: the new name of the movie(string)
    #     :return:
    #     """
    #     done = False
    #     for movie in self._movie_list:
    #         if self.find(movie.movie_id) != -1 and movie.movie_id == id:
    #             movie.time = time
    #             return movie
    #             done = True
    #     if not done:
    #         raise Exception('The given id cannot be found!')
    #
    # def find(self, id):
    #     """
    #     Search for a movie instance in the list with a matching given [id] attribute
    #     :param id: the movie's id(unique positive integer)
    #     :return: the index or -1 if there is no movie with the given id
    #     """
    #     for i in range(len(self._movie_list)):
    #         if self._movie_list[i].movie_id == id:
    #             return i
    #     return -1
    #
    # def find_movie(self, id):
    #     """
    #     Searches for a movie in the list with a matching given [id] attribute
    #     :param id: movie' s id(unique string)
    #     :return: the movie instance or raise Exception if the movie is already rented
    #     """
    #     for b in self._movie_list:
    #         if b.movie_id == id:
    #             return b
    #
    # def get_all(self):
    #     return self._movie_list[:]
    #
    # def __getitem__(self, item):
    #     return self._movie_list[item]

