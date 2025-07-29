from sqlmodel import Session, select
from ..models import Colis

class ColisRepository:
    """
    Repository class for managing Colis records in the database.

    This class provides methods to perform CRUD (Create, Read, Update, Delete) operations
    on the Colis model. It abstracts the database interactions and provides a clean
    interface for managing Colis records.

    Attributes:
        session (Session): The SQLModel session used for database operations.

    Methods:
        create_colis(colis: Colis) -> Colis:
            Adds a new Colis to the database and returns the created instance.

        get_colis(colis_id: int) -> Colis | None:
            Retrieves a Colis by its ID. Returns None if not found.

        get_all_colis(limit: int | None = None, offset: int | None = None) -> List[Colis]:
            Fetches all Colis records from the database.

        update_colis(colis_id: int, colis_update: dict) -> Colis | None:
            Updates an existing Colis with new values. Returns the updated instance
            or None if the Colis was not found.

        delete_colis(colis_id: int) -> bool:
            Deletes a Colis by its ID. Returns True if the deletion was successful,
            or False if the Colis was not found.
    """
        
    def __init__(self, session: Session):
        self.session = session

    def create_colis(self, colis: Colis) -> Colis:
        """
        Create a new Colis.

        This method adds a new Colis instance to the database and commits the transaction.

        Parameters:
            colis (Colis): The Colis instance to be created.

        Returns:
            Colis: The created Colis instance with its ID populated.
        """
        self.session.add(colis)
        self.session.commit()
        self.session.refresh(colis)
        return colis

    def get_colis(self, colis_id: int) -> Colis | None:
        """
        Retrieve a Colis by its ID.

        This method fetches a Colis from the database using its unique identifier.

        Parameters:
            colis_id (int): The ID of the Colis to retrieve.

        Returns:
            Colis | None: The Colis instance if found, otherwise None.
        """
        statement = select(Colis).where(Colis.colis_id == colis_id)
        return self.session.exec(statement).one_or_none()

    def get_all_colis(self, limit: int | None = None, offset: int | None = None) -> list[Colis]:
        """
        Retrieve all Coliss.

        This method fetches all Colis records from the database.

        Parameters:
            limit (int) : an integer to specify the maximum number of results.
            offset (int) : an integer to specify the number of lines to ignore.

        Returns:
            List[Colis]: A list of all Colis instances in the database.
        """
        statement = select(Colis).limit(limit).offset(offset)
        return list(self.session.exec(statement).all())

    def update_colis(self, colis_id: int, colis_update: dict) -> Colis | None:
        """
        Update an existing Colis.

        This method updates the fields of an existing Colis in the database
        with the values from the provided Colis instance.

        Parameters:
            colis_id (int): The ID of the Colis to update.
            colis_update (dict): The dictionary instance containing updated values.

        Returns:
            Colis | None: The updated Colis instance if found, otherwise None.
        """

        existing_colis = self.get_colis(colis_id)
        if existing_colis:
            existing_colis.sqlmodel_update(colis_update)
            self.session.add(existing_colis)
            self.session.commit()
            self.session.refresh(existing_colis)
            return existing_colis
        return None

    def delete_colis(self, colis_id: int) -> bool:
        """
        Delete a Colis by its ID.

        This method removes a Colis from the database using its unique identifier.

        Parameters:
            colis_id (int): The ID of the Colis to delete.

        Returns:
            bool: True if the deletion was successful, otherwise False.
        """
        existing_colis = self.get_colis(colis_id)
        if existing_colis:
            self.session.delete(existing_colis)
            self.session.commit()
            return True
        return False