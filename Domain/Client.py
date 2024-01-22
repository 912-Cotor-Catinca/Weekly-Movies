class Client:
    def __init__(self, client_id=0, name='', email='', phone=''):
        self._client_id = client_id
        self._name = name
        self._email = email
        self._phone = phone

    @property
    def client_id(self):
        return self._client_id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def phone(self):
        return self._phone

    @name.setter
    def name(self, other):
        self._name = other

    @email.setter
    def email(self, other):
        self._email = other

    @phone.setter
    def phone(self, other):
        self._phone = other

    def __eq__(self, other):
        return self._client_id == other

    def __str__(self):
        return str(self._client_id) + ' ' + str(self._name) + ' ' + str(self._email) + ' ' + str(self._phone)
