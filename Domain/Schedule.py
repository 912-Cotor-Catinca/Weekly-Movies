class Schedule:
    def __init__(self, schedule_id=0, movie_id=0, start_time='', day='', cinema_id=0, price=0):
        self._schedule_id = schedule_id
        self._movie_id = movie_id
        self._start_time = start_time
        self._day = day
        self._cinema_id = cinema_id
        self._price = price

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
    def day(self):
        return self._day

    @property
    def price(self):
        return self._price

    @start_time.setter
    def start_time(self, other):
        self._start_time = other

    @day.setter
    def day(self, other):
        self._day = other

    @price.setter
    def price(self, other):
        self._price=other

    def __eq__(self, other):
        return self._movie_id == other

    def __str__(self):
        return str(self._schedule_id) + ' ' + str(self._movie_id) + ' ' + str(self._cinema_id) + ' ' + str(self._start_time) + ' ' + self._day
