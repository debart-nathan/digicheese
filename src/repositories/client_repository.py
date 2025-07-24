from sqlmodel import Session, select
from ..models import Client

class ClientRepository:   
    def __init__(self, session: Session):
        self.session = session

    def create_client(self, client: Client) -> Client:
        self.session.add(client)
        self.session.commit()
        self.session.refresh(client)
        return client

    def get_client(self, client_id: int) -> Client | None:
        statement = select(Client).where(Client.client_id == client_id)
        return self.session.exec(statement).one_or_none()

    def get_all_clients(self,limit: int | None = None, offset: int | None = None ) -> list[Client]:
        statement = select(Client).limit(limit).offset(offset)
        return list(self.session.exec(statement).all())

    def update_client(self, client_id: int ,client_update: dict) -> Client | None:
        existing_client = self.get_client(client_id)
        if existing_client:
            existing_client.sqlmodel_update(client_update)
            self.session.add(existing_client)
            self.session.commit()
            self.session.refresh(existing_client)
            return existing_client
        return None

    def delete_client(self, client_id: int) -> bool:
        existing_client = self.get_client(client_id)
        if existing_client:
            self.session.delete(existing_client)
            self.session.commit()
            return True
        return False