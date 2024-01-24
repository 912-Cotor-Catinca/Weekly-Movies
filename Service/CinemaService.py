class CinemaService:
    def __init__(self, cinema_repo):
        self._cinema_repo = cinema_repo

    def get_all_cinemas(self):
        return self._cinema_repo.get_cinemas()