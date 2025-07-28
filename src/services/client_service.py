import re
from typing import Optional
from sqlmodel import Session
from ..models import ClientCreate, ClientUpdate, ClientRead, Client
from ..repositories import ClientRepository


class ClientService:
    EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    def __init__(self, session: Session):
        self.session = session
        self.repository = ClientRepository(session)

    def get_all(self, limit: int, offset: int) -> list[ClientRead]:
        clients = self.repository.get_all_clients(limit=limit,offset= offset)
        return [ClientRead.model_validate(c) for c in clients]

    def get_by_id(self, client_id: int) -> Optional[ClientRead]:
        client = self.repository.get_client(client_id)
        return ClientRead.model_validate(client) if client else None

    def create(self, client_data: ClientCreate) -> ClientRead:
        data = client_data.model_dump(exclude_unset=True)
        self.__validate_required_fields(data)
        self.__validate_email(data.get("client_email"))
        formatted_data = Client(**self.__format_data(data))
        new_client = self.repository.create_client(formatted_data)
        return ClientRead.model_validate(new_client)

    def patch(self, client_id: int, client_data: ClientUpdate) -> Optional[ClientRead]:
        if not self.repository.get_client(client_id):
            return None

        data = client_data.model_dump(exclude_unset=True)
        self.__validate_email(data.get("client_email"))
        formatted_data = self.__format_data(data)
        updated_client = self.repository.update_client(client_id, formatted_data)
        return ClientRead.model_validate(updated_client)

    def delete(self, client_id: int) -> bool:
        return self.repository.delete_client(client_id)

    @staticmethod
    def __format_data(data: dict) -> dict:
        """Format client data: capitalize first name, uppercase last name."""
        if "client_prenom" in data and data["client_prenom"]:
            data["client_prenom"] = data["client_prenom"].capitalize()
        if "client_nom" in data and data["client_nom"]:
            data["client_nom"] = data["client_nom"].upper()
        return data

    @classmethod
    def __validate_email(cls, email: Optional[str]) -> None:
        if email and not re.match(cls.EMAIL_REGEX, email):
            raise ValueError("Invalid email format.")

    @staticmethod
    def __validate_required_fields(data: dict) -> None:
        if not data.get("client_nom") or not data.get("client_prenom"):
            raise ValueError("Client 'nom' and 'prenom' are required.")
