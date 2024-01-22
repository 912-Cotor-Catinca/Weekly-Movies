
class Movie:
    def __init__(self, movie_id=0, title='', director='', genre='', duration='', cinema_id=0):
        self._movie_id = movie_id
        self._title = title
        self._director = director
        self._genre = genre
        self._duration = duration
        self._cinema_id = cinema_id

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
        return self._duration

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
        self._duration = other

    def __eq__(self, other):
        return self._movie_id == other

    def __str__(self):
        return str(self._movie_id) + ' ' + str(self._cinema_id) + ' ' + str(self._title) + ' ' + str(self._director) + ' ' + str(self._genre) + ' ' + str(self._language) + ' ' + str(self._duration) + ' ' + str(self._location)
