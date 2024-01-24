from sqlalchemy.orm import Session
from Models.models import ScheduleModel


class ScheduleRepo:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_schedules(self):
        return self.db_session.query(ScheduleModel).all()
