from sqlmodel import Session, select
from ..models import Client

class ClientRepository:
    """
    Repository class for managing Client records in the database.

    This class provides methods to perform CRUD (Create, Read, Update, Delete) operations
    on the Client model. It abstracts the database interactions and provides a clean
    interface for managing Client records.

    Attributes:
        session (Session): The SQLModel session used for database operations.

    Methods:
        create_client(client: Client) -> Client:
            Adds a new Client to the database and returns the created instance.

        get_client(client_id: int) -> Client | None:
            Retrieves a Client by its ID. Returns None if not found.

        get_all_clients(limit: int | None = None, offset: int | None = None) -> List[Client]:
            Fetches all Client records from the database.

        update_client(client_id: int, client_update: dict) -> Client | None:
            Updates an existing Client with new values. Returns the updated instance
            or None if the Client was not found.

        delete_client(client_id: int) -> bool:
            Deletes a Client by its ID. Returns True if the deletion was successful,
            or False if the Client was not found.
    """   
    def __init__(self, session: Session):
        self.session = session

    def create_client(self, client: Client) -> Client:
        """
        Create a new Client.

        This method adds a new Client instance to the database and commits the transaction.

        Parameters:
            client (Client): The Client instance to be created.

        Returns:
            Client: The created Client instance with its ID populated.
        """
        self.session.add(client)
        self.session.commit()
        self.session.refresh(client)
        return client

    def get_client(self, client_id: int) -> Client | None:
        """
        Retrieve a Client by its ID.

        This method fetches a Client from the database using its unique identifier.

        Parameters:
            client_id (int): The ID of the Client to retrieve.

        Returns:
            Client | None: The Client instance if found, otherwise None.
        """
        statement = select(Client).where(Client.client_id == client_id)
        return self.session.exec(statement).one_or_none()

    def get_all_clients(self, limit: int | None = None, offset: int | None = None ) -> list[Client]:
        """
        Retrieve all Clients.

        This method fetches all Client records from the database.

        Parameters:
            limit (int) : an integer to specify the maximum number of results.
            offset (int) : an integer to specify the number of lines to ignore.

        Returns:
            List[Client]: A list of all Client instances in the database.
        """
        statement = select(Client).limit(limit).offset(offset)
        return list(self.session.exec(statement).all())

    def update_client(self, client_id: int, client_update: dict) -> Client | None:
        """
        Update an existing Client.

        This method updates the fields of an existing Client in the database
        with the values from the provided Client instance.

        Parameters:
            client_id (int): The ID of the Client to update.
            client_update (dict): The dictionary instance containing updated values.

        Returns:
            Client | None: The updated Client instance if found, otherwise None.
        """
        existing_client = self.get_client(client_id)
        if existing_client:
            existing_client.sqlmodel_update(client_update)
            self.session.add(existing_client)
            self.session.commit()
            self.session.refresh(existing_client)
            return existing_client
        return None

    def delete_client(self, client_id: int) -> bool:
        """
        Delete a Client by its ID.

        This method removes a Client from the database using its unique identifier.

        Parameters:
            client_id (int): The ID of the Client to delete.

        Returns:
            bool: True if the deletion was successful, otherwise False.
        """
        existing_client = self.get_client(client_id)
        if existing_client:
            self.session.delete(existing_client)
            self.session.commit()
            return True
        return False