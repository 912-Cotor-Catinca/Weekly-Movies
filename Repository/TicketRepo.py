from sqlalchemy.orm import Session
from Models.models import TicketsModel


class TicketRepo:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_tickets(self):
        return self.db_session.query(TicketsModel).all()

    # def __len__(self):
    #     return len(self._ticket_list)
    #
    # def add(self, ticket):
    #     """
    #     Adds a new instance of a ticket object to the list
    #     :param ticket: the instance of the ticket object to be added
    #     :return:
    #     """
    #     if self.find(ticket.ticket_id) != -1:
    #         raise Exception('The given id does not exist')
    #     self._ticket_list.append(ticket)
    #
    # # def update(self, id, rented_date, returned_date):
    # #     done = False
    # #     for ticket in self._ticket_list:
    # #         if self.find(ticket.ticket_id) != -1 and ticket.ticket_id == id:
    # #             ticket.rented_date = rented_date
    # #             ticket.returned_date = returned_date
    # #             done = True
    # #     if not done:
    # #         raise Exception('The given id cannot be found!')
    # #
    # # def update_return(self, id, returned_date1):
    # #     """
    # #     Updates the returned date of a returned movie with the given id
    # #     :param returned_date1:
    # #     :param id: the id of the given movie to be returned
    # #     :return:
    # #     """
    # #     done = False
    # #     # returned_date1 = date.today()
    # #     for ticket in self._ticket_list:
    # #         if self.find(ticket.ticket_id) != -1 and ticket.ticket_id == id:
    # #             if ticket.returned_date == date(1, 1, 1):
    # #                 ticket.returned_date = returned_date1
    # #                 return ticket
    # #             done = True
    # #     if not done:
    # #         raise ticketRepoException('The movie cannot be returned!')
    #
    # def delete(self, id):
    #     """
    #     Deletes a ticket from the list
    #     :param id: an instance of a Ticket object
    #     :return:
    #     """
    #     index = self.find(id)
    #     if index == -1:
    #         raise Exception('The given id does not exist')
    #     del self._ticket_list[index]
    #
    # def find(self, id):
    #     """
    #     Search for a ticket instance in the list with a matching given [id] attribute
    #     :param id: the ticket's id(unique positive integer)
    #     :return: the index if the ticket exist or -1 otherwise
    #     """
    #     for i in range(len(self._ticket_list)):
    #         if self._ticket_list[i].ticket_id == id:
    #             return i
    #     return -1
    #
    # def get_all(self):
    #     return self._ticket_list[:]
    #
    # def __getitem__(self, item):
    #     return self._ticket_list[item]