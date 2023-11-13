class Ticket:
    def __init__(self, ticket_id='', movie_id='', client_id='', price=0, row=0, seat_nr=0, time='', day='',
                 location=''):
        self._ticket_id = ticket_id
        self._movie_id = movie_id
        self._client_id = client_id
        self._price = price
        self._row = row
        self._seat_nr = seat_nr
        self._time = time
        self._day = day
        self._location = location

    @property
    def ticket_id(self):
        return self._ticket_id

    @property
    def movie_id(self):
        return self._movie_id

    @property
    def client_id(self):
        return self._client_id

    @property
    def price(self):
        return self._price

    @property
    def row(self):
        return self._row

    @property
    def seat_nr(self):
        return self._seat_nr

    @property
    def time(self):
        return self._time

    @property
    def day(self):
        return self._day

    @property
    def location(self):
        return self._location

    @price.setter
    def price(self, other):
        self._price = other

    @row.setter
    def row(self, other):
        self._row = other

    @seat_nr.setter
    def seat_nr(self, other):
        self._seat_nr = other

    @time.setter
    def time(self, other):
        self._time = other

    @day.setter
    def day(self, other):
        self._day = other

    @location.setter
    def location(self, other):
        self._location = other

    def __eq__(self, other):
        return self._client_id == other

    def __str__(self):
        return self._ticket_id + ' ' + str(self._movie_id) + ' ' + str(self._client_id) + ' ' + str(self._price) + ' ' + str(
            self._row) + ' ' + str(self._seat_nr) + ' ' + self._day + ' ' + self._time + ' ' + self._location
