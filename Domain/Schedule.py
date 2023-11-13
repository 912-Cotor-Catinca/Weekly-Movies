class Schedule:
    def __init__(self, schedule_id='', movie_id='', start_time='', available_seats=0, day='', location=''):
        self._schedule_id = schedule_id
        self._movie_id = movie_id
        self._start_time = start_time
        self._available_seats = available_seats
        self._day = day
        self._location = location

    @property
    def schedule_id(self):
        return self._schedule_id

    @property
    def movie_id(self):
        return self._movie_id

    @property
    def start_time(self):
        return self._start_time

    @property
    def available_seats(self):
        return self._available_seats

    @property
    def location(self):
        return self._location

    @property
    def day(self):
        return self._day

    @start_time.setter
    def start_time(self, other):
        self._start_time = other

    @available_seats.setter
    def available_seats(self, other):
        self._available_seats = other

    @location.setter
    def location(self, other):
        self._location = other

    @day.setter
    def day(self, other):
        self._day = other

    def __eq__(self, other):
        return self._movie_id == other

    def __str__(self):
        return self._schedule_id + ' ' + str(self._movie_id) + ' ' + str(self._start_time) + ' ' + str(
            self._available_seats) + ' ' + self._day + '' + self._location
