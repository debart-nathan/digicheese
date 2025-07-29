import re
from typing import Optional
from sqlmodel import Session
from ..models import ClientCreate, ClientUpdate, ClientRead, Client
from ..repositories import ClientRepository


class ClientService:
    """
    Service class for managing client operations.

    This class provides methods to create, read, update, and delete clients
    in the database. It utilizes the ClientRepository for database interactions
    and performs validation on client data.

    Attributes:
        session (Session): The SQLAlchemy session for database operations.
        repository (ClientRepository): The repository for client-related database operations.
    """

    EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    def __init__(self, session: Session):
        """
        Initializes the ClientService with a database session.

        Args:
            session (Session): The SQLAlchemy session to be used for database operations.
        """
        self.session = session
        self.repository = ClientRepository(session)

    def get_all(self, limit: int, offset: int) -> list[ClientRead]:
        """
        Retrieves all clients with pagination.

        Args:
            limit (int): The maximum number of clients to return.
            offset (int): The number of clients to skip before starting to collect the result set.

        Returns:
            list[ClientRead]: A list of ClientRead objects representing the clients.
        """
        clients = self.repository.get_all_clients(limit=limit, offset=offset)
        return [ClientRead.model_validate(c) for c in clients]

    def get_by_id(self, client_id: int) -> Optional[ClientRead]:
        """
        Retrieves a client by its ID.

        Args:
            client_id (int): The ID of the client to retrieve.

        Returns:
            Optional[ClientRead]: A ClientRead object representing the client, or None if not found.
        """
        client = self.repository.get_client(client_id)
        return ClientRead.model_validate(client) if client else None

    def create(self, client_data: ClientCreate) -> ClientRead:
        """
        Creates a new client in the database.

        Args:
            client_data (ClientCreate): The data for the new client.

        Returns:
            ClientRead: A ClientRead object representing the created client.

        Raises:
            ValueError: If required fields are missing or if the email format is invalid.
        """
        data = client_data.model_dump(exclude_unset=True)
        self.__validate_required_fields(data)
        self.__validate_email(data.get("client_email"))
        formatted_data = Client(**self.__format_data(data))
        new_client = self.repository.create_client(formatted_data)
        return ClientRead.model_validate(new_client)

    def patch(self, client_id: int, client_data: ClientUpdate) -> Optional[ClientRead]:
        """
        Updates an existing client in the database.

        Args:
            client_id (int): The ID of the client to update.
            client_data (ClientUpdate): The data to update the client with.

        Returns:
            Optional[ClientRead]: A ClientRead object representing the updated client, or None if not found.

        Raises:
            ValueError: If the email format is invalid.
        """
        if not self.repository.get_client(client_id):
            return None

        data = client_data.model_dump(exclude_unset=True)
        self.__validate_email(data.get("client_email"))
        formatted_data = self.__format_data(data)
        updated_client = self.repository.update_client(client_id, formatted_data)
        return ClientRead.model_validate(updated_client)

    def delete(self, client_id: int) -> bool:
        """
        Deletes a client from the database.

        Args:
            client_id (int): The ID of the client to delete.

        Returns:
            bool: True if the client was successfully deleted, False otherwise.
        """
        return self.repository.delete_client(client_id)

    @staticmethod
    def __format_data(data: dict) -> dict:
        """
        Formats client data by capitalizing the first name and uppercasing the last name.

        Args:
            data (dict): The client data to format.

        Returns:
            dict: The formatted client data.
        """
        if "client_prenom" in data and data["client_prenom"]:
            data["client_prenom"] = data["client_prenom"].capitalize()
        if "client_nom" in data and data["client_nom"]:
            data["client_nom"] = data["client_nom"].upper()
        return data

    @classmethod
    def __validate_email(cls, email: Optional[str]) -> None:
        """
        Validates the email format.

        Args:
            email (Optional[str]): The email to validate.

        Raises:
            ValueError: If the email format is invalid.
        """
        if email and not re.match(cls.EMAIL_REGEX, email):
            raise ValueError("Invalid email format.")

    @staticmethod
    def __validate_required_fields(data: dict) -> None:
        """
        Validates that required fields are present in the client data.

        Args:
            data (dict): The client data to validate.

        Raises:
            ValueError: If the 'client_nom' or 'client_prenom' fields are missing or empty.
        """
        if not data.get("client_nom") or not data.get("client_prenom"):
            raise ValueError("Client 'nom' and 'prenom' are required.")

