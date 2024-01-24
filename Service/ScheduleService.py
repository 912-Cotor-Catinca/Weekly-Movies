
class ScheduleService:
    def __init__(self, schedule_repo):
        self._schedule_repo = schedule_repo

    def get_all_schedules(self):
        return self._schedule_repo.get_schedules()