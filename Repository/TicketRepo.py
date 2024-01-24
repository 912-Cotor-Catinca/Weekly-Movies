from sqlalchemy.orm import Session
from Models.models import TicketsModel


class TicketRepo:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_tickets(self):
        return self.db_session.query(TicketsModel).all()
