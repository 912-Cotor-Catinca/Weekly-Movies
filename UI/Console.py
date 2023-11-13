import datetime
from random import randrange, choice, randint


class UI:
    def __init__(self, srv_movie, srv_client, srv_ticket):
        self._srvMovie = srv_movie
        self._srvClient = srv_client
        self._srvTicket = srv_ticket
        self._commands = {'add_movie': self._add_movie_ui, 'list_movies': self._display_movies,
                          'delete_movie': self._delete_movie, 'update_movie': self._update_movie,
                          'list_clients': self._display_clients, 'delete_client': self._delete_client, 'update_client':
                              self._update_client, 'list_tickets': self._display_tickets,
                          'add_client': self._add_client_ui,
                          'return_movie': self._return_movie, 'buy_movie': self._rent_movie,
                          'statistic1': self._statistic1,
                          'statistic2': self._statistic3,
                          'search_by_client_name': self._search_client_name, 'search_by_title': self._search_by_title,
                          'search_by_director': self._search_by_director, 'search_by_movie_id': self._search_movie_id,
                          'search_by_client_id': self._search_client_id}
        self.test_init_clients()
        self.test_init_movies()
        self.test_init_tickets()

    @staticmethod
    def print_menu():
        print('\t Movie tickets Register')
        print('\033[4m' + "movie Data:" + '\033[m')
        print('\t To add a new movie use ''add_movie'' command')
        print('\t To list all movies use list_movies command')
        print('\t To delete a movie use ''delete_movie'' command')
        print('\t To update a movie parameters use ''update_movie'' command')
        print('\t To search by id movie use ''search_by_movie_id'' command')
        print('\t To search by title use ''search_by_title'' command')
        print('\t To search by author use ''search_by_author'' command')
        print('\033[4m' + "Client Data:" + '\033[m')
        print('\t To add a new client use ''add_client'' command')
        print('\t To list all client use ''list_clients'' command')
        print('\t To delete a client use ''delete_movie'' command')
        print('\t To update a client parameters use ''update_movie'' command')
        print('\t To search by id client use ''search_by_client_id'' command')
        print('\t To search by name use ''search_by_name'' command')
        print('\033[4m' + "Ticket Data:" + '\033[m')
        print('\t To list all tickets use ''list_tickets'' command')
        print('\t To add a new client use ''add_client'' command')
        print('\t To rent a movie ''rent_movie'' command')
        print('\t To return a movie ''return_movie'' command\n')
        print('\033[4m' + "Statistics:" + '\033[m')
        print('\t To see the most rented movies use ''statistic1'' command')
        print('\t To see the most active clients use ''statistic2'' command')

    def split_command(self, command):
        command = command.strip()
        tokens = command.split(' ', 1)
        cmd_word = tokens[0].strip()
        cmd_params = tokens[1].strip if len(tokens) == 2 else ''
        return cmd_word, cmd_params

    def read_movie(self):
        movie_id = None
        title = None
        director = None
        genre = None
        time = None
        language = None
        location = None
        try:
            movie_id = input('id: ')
            title = input('title: ')
            director = input('director: ')
            genre = input('genre: ')
            time = input('time: ')
            language = input('language: ')
            location = input('location: ')
        except ValueError:
            print('Invalid parameters')
        return [movie_id, title, director, genre, time, language, location]

    def read_client(self):
        client_id = None
        name = None
        email = None
        phone = None
        try:
            client_id = input('id: ')
            name = input('name: ')
            email = input('email: ')
            phone = input('phone: ')
        except ValueError:
            print('Invalid Parameters!')
        return [client_id, name, email, phone]

    def read_ticket(self):
        ticket_id = None
        ticket_date = None
        movie_id = None
        client_id = None
        returned_date = None
        try:
            ticket_id = int(input('id_ticket: '))
            movie_id = input('id_movie: ')
            client_id = int(input('id_client: '))
            ticket_date = datetime.date.today()
            returned_date = datetime.date(1, 1, 1)
        except ValueError:
            print('Invalid Parameters!')
        return [ticket_id, movie_id, client_id, ticket_date, returned_date]

    def start_uit(self):
        self.print_menu()

        done = False
        while not done:
            command = input('command>')
            if command == 'exit':
                return
            cmd_word, cmd_params = self.split_command(command)
            if command in self._commands:
                try:
                    self._commands[cmd_word](cmd_params)
                except ValueError:
                    print('Invalid Parameters')

            else:
                print('Bad command!')

    def _add_movie_ui(self, params):
        done = False
        while not done:
            b = self.read_movie()
            movie = self._srvMovie.add_movie(b[0], b[1], b[2], b[3], b[4], b[5], b[6])
            return movie
            cmd = input()
            if cmd == 's' or cmd == 'S':
                done = True

    def _display_movies(self, params):
        movie = self._srvMovie.display()
        if len(movie) == 0:
            print('no movies')
            return
        for b in movie:
            print(b)

    def _delete_movie(self, params):
        movie_id = input('movie id: ')
        if self._srvTicket.find_movie_id(movie_id) == -1:
            self._srvMovie.delete_movie(movie_id)
        else:
            self._srvTicket.delete_movie_tickets(movie_id)

    def _add_client_ui(self, params):
        done = False
        while not done:
            c = self.read_client()
            client = self._srvClient.add_client(c[0], c[1])

            cmd = input()
            if cmd == 's' or cmd == 'S':
                done = True
            return client

    def _display_tickets(self, params):
        ticket = self._srvTicket.display()
        if len(ticket) == 0:
            print('no tickets')
            return
        for r in ticket:
            print(r)

    def _display_clients(self, params):
        client = self._srvClient.display()
        if len(client) == 0:
            print('no clients')
            return
        for c in client:
            print(c)

    def _delete_client(self, params):
        client_id = int(input('id: '))
        if self._srvTicket.find_client_id(client_id) == -1:
            self._srvClient.delete_client(client_id)
        else:
            self._srvTicket.delete_client_and_its_tickets(client_id)

    def _return_movie(self, params):
        ticket_id = int(input('id_ticket: '))
        if self._srvTicket.find_id_ticket(ticket_id) != -1:
            self._srvTicket.update_return(ticket_id, datetime.date.today())
        else:
            print('The given id was not found')

    def _rent_movie(self, params):
        r = self.read_ticket()
        if self._srvTicket.check_if_rent(r[1], r[4]):
            rent = self._srvTicket.add_ticket(r[0], r[1], r[2], r[3], r[4])
            return rent
        else:
            print('The movie cannot be rented')

    def _update_client(self, params):
        id = int(input('id: '))
        if self._srvClient.find(id) != -1:
            name = input('name: ')
            client = self._srvClient.update_client(id, name)
            return client
        else:
            print('The given id does not exist')

    def test_init_clients(self):
        surname_list = ['Pop', 'Ionescu', 'Popescu', 'Moldovan', 'Oltean', 'Stan', 'Rus', 'Rusu', 'Toma', 'Petrescu']
        forename_list = ['Ana', 'Dana', 'Dan', 'Sara', 'Vlad', 'Maria', 'Ion', 'Luca', 'Radu', 'Mihai']
        for i in range(1, 11):
            name = surname_list[randrange(9)] + " " + forename_list[randrange(9)]
            self._srvClient.add_client(str(i), name, "email", "phone")
        return self._srvClient

    def test_init_tickets(self):
        movie_id = ['1', '2', '3', '4']
        client_id = ['1', '2', '3', '4', '5', '6']
        for i in range(1, 11):
            id_movie = choice(movie_id)
            id_client = choice(client_id)
            row = randint(1, 20)
            seat_nr = randint(1, 15)
            self._srvTicket.add_ticket(str(i), id_movie, id_client, "20", str(row), str(seat_nr), "19:00", "Monday")
        return self._srvTicket

    def test_init_movies(self):
        movies = [
            {"name": "The Shawshank Redemption", "director": "Frank Darabont", "genre": "Drama", "time": "200",
             "language": "English", "location": "United States"},
            {"name": "Inception", "director": "Christopher Nolan", "genre": "Sci-Fi, Action", "time": "2010",
             "language": "English", "location": "Worldwide"},
            {"name": "Spirited Away", "director": "Hayao Miyazaki", "genre": "Animation, Fantasy", "time": "120",
             "language": "Japanese", "location": "Japan"},
            {"name": "The Godfather", "director": "Francis Ford Coppola", "genre": "Crime, Drama", "time": "1972",
             "language": "English", "location": "United States"},
            {"name": "Pulp Fiction", "director": "Quentin Tarantino", "genre": "Crime, Drama", "time": "1994",
             "language": "English", "location": "United States"},
            {"name": "The Dark Knight", "director": "Christopher Nolan", "genre": "Action, Crime", "time": "2008",
             "language": "English", "location": "United States"},
            {"name": "The Matrix", "director": "Lana Wachowski, Lilly Wachowski", "genre": "Action, Sci-Fi",
             "time": "1999", "language": "English", "location": "United States"},
            {"name": "Forrest Gump", "director": "Robert Zemeckis", "genre": "Drama, Romance", "time": "1994",
             "language": "English", "location": "United States"},
            {"name": "The Lord of the Rings: The Fellowship of the Ring", "director": "Peter Jackson",
             "genre": "Action, Adventure", "time": "2001", "language": "English", "location": "New Zealand"},
            {"name": "The Grand Budapest Hotel", "director": "Wes Anderson", "genre": "Adventure, Comedy",
             "time": "2014", "language": "English", "location": "Various"},
        ]

        for i in range(1, 11):
            movie = choice(movies)
            movies.remove(movie)
            title = movie["name"]
            director = movie["director"]
            genre = movie["genre"]
            time = movie["time"]
            language = movie["language"]
            location = movie["location"]
            self._srvMovie.add_movie(str(i), title, director, genre, time, language, location)
        return self._srvMovie

    def _update_movie(self, params):
        movie_id = input('id: ')
        if self._srvMovie.find(movie_id) != -1:
            title = input('title: ')
            author = input('author: ')
            self._srvMovie.update_movie(movie_id, title, author)
        else:
            print('The given id cannot be found')

    def _statistic1(self, params):
        print("Most rented movie. The list of movie sorted in descending order by number of times they were rented")
        data = self._srvTicket.most_booked_movies()
        if len(data) == 0:
            print('No tickets')
        else:
            for movie in data:
                print(movie)

    def _statistic3(self, params):
        print("Most active clients. The list of clients sorted in descending order by the number of movie ticket days "
              "they have ")
        data = self._srvTicket.most_cinephile_clients()
        if len(data) == 0:
            print('No tickets')
        else:
            for client in data:
                print(client)

    def _search_client_name(self, params):
        name = input('Client Name: ')
        result = self._srvClient.search_client_name(name)
        if len(result) == 0:
            print('No matches!')
            return
        for c in result:
            print(c)

    def _search_by_director(self, params):
        director = input('Director: ')
        result = self._srvMovie.search_director(director)
        if len(result) == 0:
            print('No matches!')
            return
        for r in result:
            print(r)

    def _search_by_title(self, params):
        title = input('Title: ')
        result = self._srvMovie.search_title(title)
        if len(result) == 0:
            print('No matches!')
            return
        for r in result:
            print(r)

    def _search_movie_id(self, params):
        movie_id = input('movie id: ')
        result = self._srvMovie.search_id(movie_id)
        if len(result) == 0:
            print('No matches!')
            return
        for r in result:
            print(r)

    def _search_client_id(self, params):
        client_id = int(input('Client ID: '))
        result = self._srvClient.search_id(client_id)
        if len(result) == 0:
            print('No matches!')
            return
        for r in result:
            print(r)
