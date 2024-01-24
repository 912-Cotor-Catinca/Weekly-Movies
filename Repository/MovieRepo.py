from sqlalchemy.orm import Session
from Models.models import MovieModel


class MovieRepo:
    def __init__(self, db_session):
        # self._movie_list = []
        self.db_session = db_session

    def get_movies(self):
        return self.db_session.query(MovieModel).all()

    def get_movies_by_cinema(self, cinemaid):
        return self.db_session.query(MovieModel).filter_by(cinemaid=cinemaid).all()

    def get_movies_by_genre(self, genre):
        return self.db_session.query(MovieModel).filter(MovieModel.genre.like(f"%{genre}%")).all()
