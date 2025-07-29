from sqlmodel import Session, select
from ..models import Commune

class CommuneRepository:
    """
    Repository class for managing Commune records in the database.

    This class provides methods to perform CRUD (Create, Read, Update, Delete) operations
    on the Commune model. It abstracts the database interactions and provides a clean
    interface for managing Commune records.

    Attributes:
        session (Session): The SQLModel session used for database operations.

    Methods:
        create_commune(commune: Commune) -> Commune:
            Adds a new Commune to the database and returns the created instance.

        get_commune(commune_id: int) -> Commune | None:
            Retrieves a Commune by its ID. Returns None if not found.

        get_all_communes(limit: int | None = None, offset: int | None = None) -> List[Commune]:
            Fetches all Commune records from the database.

        update_commune(commune_id: int, commune_update: dict) -> Commune | None:
            Updates an existing Commune with new values. Returns the updated instance
            or None if the Commune was not found.

        delete_commune(commune_id: int) -> bool:
            Deletes a Commune by its ID. Returns True if the deletion was successful,
            or False if the Commune was not found.
    """
        
    def __init__(self, session: Session):
        self.session = session

    def create_commune(self, commune: Commune) -> Commune:
        """
        Create a new Commune.

        This method adds a new Commune instance to the database and commits the transaction.

        Parameters:
            commune (Commune): The Commune instance to be created.

        Returns:
            Commune: The created Commune instance with its ID populated.
        """
        self.session.add(commune)
        self.session.commit()
        self.session.refresh(commune)
        return commune

    def get_commune(self, commune_id: int) -> Commune | None:
        """
        Retrieve a Commune by its ID.

        This method fetches a Commune from the database using its unique identifier.

        Parameters:
            commune_id (int): The ID of the Commune to retrieve.

        Returns:
            Commune | None: The Commune instance if found, otherwise None.
        """
        statement = select(Commune).where(Commune.commune_id == commune_id)
        return self.session.exec(statement).one_or_none()

    def get_all_communes(self, limit: int | None = None, offset: int | None = None) -> list[Commune]:
        """
        Retrieve all Communes.

        This method fetches all Commune records from the database.

        Parameters:
            limit (int) : an integer to specify the maximum number of results.
            offset (int) : an integer to specify the number of lines to ignore.

        Returns:
            List[Commune]: A list of all Commune instances in the database.
        """
        statement = select(Commune).limit(limit).offset(offset)
        return list(self.session.exec(statement).all())

    def update_commune(self, commune_id: int, commune_update: dict) -> Commune | None:
        """
        Update an existing Commune.

        This method updates the fields of an existing Commune in the database
        with the values from the provided Commune instance.

        Parameters:
            commune_id (int): The ID of the Commune to update.
            commune_update (dict): The Commune instance containing updated values.

        Returns:
            Commune | None: The updated Commune instance if found, otherwise None.
        """

        existing_commune = self.get_commune(commune_id)
        if existing_commune:
            existing_commune.sqlmodel_update(commune_update)
            self.session.add(existing_commune)
            self.session.commit()
            self.session.refresh(existing_commune)
            return existing_commune
        return None

    def delete_commune(self, commune_id: int) -> bool:
        """
        Delete a Commune by its ID.

        This method removes a Commune from the database using its unique identifier.

        Parameters:
            commune_id (int): The ID of the Commune to delete.

        Returns:
            bool: True if the deletion was successful, otherwise False.
        """
        existing_commune = self.get_commune(commune_id)
        if existing_commune:
            self.session.delete(existing_commune)
            self.session.commit()
            return True
        return False