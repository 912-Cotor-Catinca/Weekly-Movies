
from Models.models import TicketsModel


class TicketRepo:
    def __init__(self, db_session):
        self.db_session = db_session


    def get_tickets(self):
        return self.db_session.query(TicketsModel).all()

    def add_ticket(self, ticket):
        self.db_session.add(ticket)
        self.db_session.commit()
        self.db_session.refresh(ticket)
        return ticket
