from sqlalchemy.orm import Session
from Models.models import ClientModel


class ClientRepo:
    def __init__(self, db_session):
        # self._client_list = []
        self.db_session = db_session

    def get_clients(self):
        return self.db_session.query(ClientModel).all()

    def create_client(self, name, email, phone):
        new_client = ClientModel(name=name, email=email, phone=phone)
        self.db_session.add(new_client)
        self.db_session.commit()
        self.db_session.refresh(new_client)
        return new_client