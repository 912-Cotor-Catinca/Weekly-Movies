class ScheduleService:
    pass

class ScheduleService:
    def __init__(self, schedule_repo):
        self._schedule_repo = schedule_repo

    def get_all_schedules(self):
        return self._schedule_repo.get_schedules()

    def get_schedule_by_cinema(self, cinemaid):
        return self._schedule_repo.get_schedules_by_cinema(cinemaid)

    def get_schedule_by_genre(self, genre):
        return self._schedule_repo.get_schedules_by_genre(genre)

    def filter_by_genre_and_cinema(self, genre, cinemaid):
        return self._schedule_repo.filter_by_genre_and_cinema(genre, cinemaid)

