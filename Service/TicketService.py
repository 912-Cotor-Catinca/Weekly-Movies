from Domain.Ticket import Ticket, TicketDTO



class TicketService:
    def __init__(self, ticket_repo):
        self._ticket_repo = ticket_repo

    def get_all_tickets(self):
        return self._ticket_repo.get_tickets()
