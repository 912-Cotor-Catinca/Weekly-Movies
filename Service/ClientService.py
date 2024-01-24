from Domain.Client import Client


class ClientService:
    def __init__(self, client_repo):
        self._client_repo = client_repo

    def get_all_clients(self):
        return self._client_repo.get_clients()

    def add_client(self, name, email, phone):
        """
        Instantiates a Client object with a given [client_movie], a[name] and adds it to the repo
        :param phone: Client's phone
        :param email: Client's email
        :param name: Client's title
        :return:
        """
        return self._client_repo.create_client(name, email, phone)


