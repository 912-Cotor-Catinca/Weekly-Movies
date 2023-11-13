
class Movie:
    def __init__(self, movie_id='', title='', director='', genre='', time='', language='', location=''):

        self._movie_id = movie_id
        self._title = title
        self._director = director
        self._genre = genre
        self._time = time
        self._language = language
        self._location = location

    @property
    def movie_id(self):
        return self._movie_id

    @property
    def title(self):
        return self._title

    @property
    def director(self):
        return self._director

    @property
    def genre(self):
        return self._genre

    @property
    def time(self):
        return self._time

    @property
    def language(self):
        return self._language

    @property
    def location(self):
        return self._location

    @title.setter
    def title(self, other):
        self._title = other

    @director.setter
    def director(self, other):
        self._director = other

    @genre.setter
    def genre(self, other):
        self._genre = other

    @time.setter
    def time(self, other):
        self._time = other

    @language.setter
    def language(self, other):
        self._language = other

    @location.setter
    def location(self, other):
        self._location = other

    def __eq__(self, other):
        return self._movie_id == other

    def __str__(self):
        return str(self._movie_id) + ' ' + str(self._title) + ' ' + str(self._director) + ' ' + str(self._genre) + ' ' + str(self._language) + ' ' + str(self._time) + ' ' + str(self._location)
