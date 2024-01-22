from Domain.Ticket import Ticket, TicketDTO


class MovieTicketCountDTO:
    def __init__(self, movie, count):
        self._movie = movie
        self._count = count

    @property
    def movie(self):
        return self._movie

    @property
    def count(self):
        return self._count

    def __str__(self):
        return str(self._movie) + ' ' + str(self._count)


class ClientTicketDTO:
    def __init__(self, client, days):
        self._client = client
        self._days = days

    @property
    def client(self):
        return self._client

    @property
    def days(self):
        return self._days

    def __str__(self):
        return str(self._client) + ' ' + str(self._days)


class MovieAuthorCountDTO:
    def __init__(self, author, count):
        self._author = author
        self._count = count

    @property
    def author(self):
        return self._author

    @property
    def count(self):
        return self._count

    def __str__(self):
        return self.author + ' ' + str(self.count)


class TicketService:
    def __init__(self, ticket_repo, movie_repo, client_repo):
        self._ticket_repo = ticket_repo
        self._movie_repo = movie_repo
        self._client_repo = client_repo

    def add_ticket(self, id_ticket, id_movie, id_client, price, row, seat_nr, time, day):
        """
        Adds in a list if a client rented a movie
        :param day: Ticket's day
        :param time: Ticket's time
        :param seat_nr: Ticket's seat number
        :param row: Ticket's row
        :param price: Ticket's price
        :param id_ticket: Ticket's id
        :param id_movie: Ticket's movie id
        :param id_client: Ticket's client id
        :return:
        """
        movie = self._movie_repo.find_movie(id_movie)
        client = self._client_repo.find_client(id_client)
        ticket = Ticket(id_ticket, movie, client, price, row, seat_nr, time, day)
        if self.find_id_ticket(ticket.ticket_id) != -1:
            raise ValueError('Ticket already exists!')
        else:
            self._ticket_repo.add(ticket)
        return ticket

    def delete_ticket(self, ticket_id, true=False):
        ticket = self._ticket_repo.delete(ticket_id)
        return ticket

    def delete_client_and_its_tickets(self, id_client):
        tickets = self._ticket_repo.get_all()
        to_delete = []
        for ticket in tickets:
            if ticket.client.client_id == id_client:
                to_delete.append(ticket)
                self._ticket_repo.delete(ticket.ticket_id)
        self._client_repo.delete(id_client)
        return to_delete

    def delete_movie_tickets(self, id_movie):
        tickets = self._ticket_repo.get_all()
        to_delete = []
        for ticket in tickets:
            if ticket.get_movie == id_movie:
                to_delete.append(ticket)
                self._ticket_repo.delete(ticket.ticket_id)
        self._movie_repo.delete(id_movie)
        return to_delete

    def display(self):
        """
        Display the ticket list
        :return:
        """
        ticket = self._ticket_repo.get_all()
        ticket_dtos = []
        for r in ticket:
            id_ticket = r.ticket_id
            movie_id = r.movie_id.title
            client_id = r.client_id.name
            price = r.price
            time = r.time
            day = r.day
            ticket_dto = TicketDTO(id_ticket, movie_id, client_id, price, day, time)
            ticket_dtos.append(ticket_dto)
        return ticket_dtos

    def find_id_ticket(self, id):
        """
        Search the given id_ticket is in the list of tickets
        :param id: The ticket's id
        :return: the index of the ticket or -1 if there does not exist
        """
        for i in range(len(self._ticket_repo)):
            if self._ticket_repo[i].ticket_id == id:
                return i
        return -1

    def find_client_id(self, id_client):
        for i in range(len(self._ticket_repo)):
            if self._ticket_repo[i].client.client_id == id_client:
                return i
        return -1

    def find_movie_id(self, movie_id):
        for i in range(len(self._ticket_repo)):
            if self._ticket_repo[i].get_movie == movie_id:
                return i
        return -1

    def most_booked_movies(self):
        """
        The list of movies, sorted in descending order by the number of times they were booked
        :return: A list of movies
        """
        result = []
        for movie in self._movie_repo.get_all():
            dto = MovieTicketCountDTO(movie, self._create_movie_ticket_count(movie))
            result.append(dto)

        result.sort(reverse=True, key=lambda movie_dto: movie_dto.count)
        return result

    def most_cinephile_clients(self):
        """
        The list of clients, sorted in descending order by the number of movie tickets they've booked
        :return: A list of clients
        """
        result = []
        for client in self._client_repo.get_all():
            count = 0
            for ticket in self._ticket_repo.get_all():
                if client.client_id == ticket.client_id.client_id:
                    count += 1
            days = count
            dto = ClientTicketDTO(client, days)
            result.append(dto)

        result.sort(reverse=True, key=lambda client_dto: client_dto.days)
        return result

    def _create_movie_ticket_count(self, movie):
        return len(self.filter_tickets(None, movie))

    def _create_client_count(self, client):
        return len(self.filter_tickets(client, None))

    def filter_tickets(self, client, movie):
        """
        Return a list of tickets performed by the provided client for the provided movie
        client - The client performing the ticket. None means all clients
        movie - The rented movie. None means all movies
        :param client:
        :param movie:
        :return:
        """
        result = []
        for ticket in self._ticket_repo.get_all():
            if client is not None and ticket.client_id != client:
                continue
            if movie is not None and ticket.movie_id != movie:
                continue
            result.append(ticket)
        return result

