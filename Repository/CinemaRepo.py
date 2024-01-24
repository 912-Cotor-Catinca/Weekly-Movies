from sqlalchemy.orm import Session
from Models.models import CinemaModel


class CinemaRepo:
    def __init__(self, db_session):
        # self._client_list = []
        self.db_session = db_session

    def get_cinemas(self):
        return self.db_session.query(CinemaModel).all()