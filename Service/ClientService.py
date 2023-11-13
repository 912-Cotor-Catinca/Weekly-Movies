from Domain.Client import Client


class ClientService:
    def __init__(self, client_repo):
        self._client_repo = client_repo

    def add_client(self, client_id, name, email, phone):
        """
        Instantiates a Client object with a given [client_movie], a[name] and adds it to the repo
        :param phone: Client's phone
        :param email: Client's email
        :param client_id: The Client's id
        :param name: Client's title
        :return:
        """
        client = Client(client_id, name, email, phone)
        if self.find(client.client_id) != -1:
            raise ValueError('Client already exists!')
        else:
            self._client_repo.add(client)
        return client

    def update_client(self, id, name):
        """
       Updates the name of an instance of a Client object with a given id
       :param id: Client's id
       :param name: Client's name
       :return:
       """
        for c in self._client_repo.get_all():
            if c.client_id == id:
                old_name = c.name
        new_client = self._client_repo.update(id, name)
        return new_client, old_name

    def display(self):
        """
        Return a shallow copy of the list
        :return: the list of clients
        """
        return self._client_repo.get_all()

    def delete_client(self, id):
        """
        Deletes a Client object with the given [id]
        :param id: the client's id to be deleted
        :return:
        """
        client = self._client_repo.delete(id)
        return client

    def find(self, id):
        """
        Find by id a client
        :param id: Client's id
        :return: the index if there exist or -1 otherwise
        """
        for i in range(len(self._client_repo)):
            if self._client_repo[i].client_id == id:
                return i
        return -1

    def search_client_name(self, name):
        result = []
        for c in self._client_repo.get_all():
            if name.lower() in c.name.lower():
                result.append(c)
        return result

    def search_id(self, client_id):
        result = []
        id = str(client_id)
        for c in self._client_repo.get_all():
            client = str(c.client_id)
            if id.lower() in client.lower():
                result.append(c)
        return result
