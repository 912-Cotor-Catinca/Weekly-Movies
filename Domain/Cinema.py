
class Movie:
    def __init__(self, cinema_id=0, name='', location='', rows = 0, columns = 0):
        self._cinema_id = cinema_id
        self._name = name
        self._location = location
        self._rows = rows
        self._columns = columns

    @property
    def cinema_id(self):
        return self._cinema_id

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    @name.setter
    def name(self, other):
        self._name = other

    @location.setter
    def location(self, other):
        self._location = other

    @rows.setter
    def rows(self, other):
        self._rows = other

    @columns.setter
    def columns(self, other):
        self._columns = other

    def __eq__(self, other):
        return self._cinema_id == other

    def __str__(self):
        return str(self._cinema_id) + ' ' + str(self._name) + ' ' + str(self._location) + ' ' + str(self._rows) + ' ' + str(self._columns)
