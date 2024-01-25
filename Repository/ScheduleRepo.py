from sqlalchemy.orm import Session
from Models.models import ScheduleModel, MovieModel


class ScheduleRepo:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_schedules(self):
        return self.db_session.query(ScheduleModel).all()

    def get_schedules_by_cinema(self, cinemaid):
        return self.db_session.query(ScheduleModel).filter_by(cinemaid=cinemaid).all()

    def get_schedules_by_genre(self, genre):
        return (
            self.db_session.query(ScheduleModel)
            .join(ScheduleModel.movie)
            .filter(MovieModel.genre.like(f"%{genre}%"))
            .all()
        )

    def filter_by_genre_and_cinema(self, genre, cinemaid):
        return (
            self.db_session.query(ScheduleModel)
                .join(ScheduleModel.movie)
                .filter(MovieModel.genre.like(f"%{genre}%"))
                .filter(ScheduleModel.cinemaid == cinemaid)
                .all()
        )