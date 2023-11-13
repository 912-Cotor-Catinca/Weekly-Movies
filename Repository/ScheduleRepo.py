class ScheduleRepo:
    def __init__(self):
        self._schedule_list = []

    def __len__(self):
        return len(self._schedule_list)

    def add(self, schedule):
        """
        Adds a new instance of a Schedule object to the list
        :param schedule: the instance of the Rental object to be added
        :return:
        """
        if self.find(schedule.schedule_id) != -1:
            raise Exception('The given id does not exist')
        self._schedule_list.append(schedule)

    def delete(self, id):
        """
        Deletes a schedule from the list
        :param id: an instance of a Schedule object
        :return:
        """
        index = self.find(id)
        if index == -1:
            raise Exception('The given id does not exist')
        del self._schedule_list[index]

    def find(self, id):
        """
        Search for a schedule instance in the list with a matching given [id] attribute
        :param id: the schedule's id(unique positive integer)
        :return: the index if the rental exist or -1 otherwise
        """
        for i in range(len(self._schedule_list)):
            if self._schedule_list[i].ticket_id == id:
                return i
        return -1

    def get_all(self):
        return self._schedule_list[:]

    def __getitem__(self, item):
        return self._schedule_list[item]
