from sqlmodel import Session, select
from ..models import Objet

class ObjetRepository:
    """
    Repository class for managing Objet records in the database.

    This class provides methods to perform CRUD (Create, Read, Update, Delete) operations
    on the Objet model. It abstracts the database interactions and provides a clean
    interface for managing Objet records.

    Attributes:
        session (Session): The SQLModel session used for database operations.

    Methods:
        create_objet(objet: Objet) -> Objet:
            Adds a new Objet to the database and returns the created instance.

        get_objet(objet_id: int) -> Objet | None:
            Retrieves a Objet by its ID. Returns None if not found.

        get_all_objets(limit: int | None = None, offset: int | None = Non) -> List[Objet]:
            Fetches all Objet records from the database.

        update_objet(objet_id: int, objet_update: dict) -> Objet | None:
            Updates an existing Objet with new values. Returns the updated instance
            or None if the Objet was not found.

        delete_objet(objet_id: int) -> bool:
            Deletes a Objet by its ID. Returns True if the deletion was successful,
            or False if the Objet was not found.
    """
        
    def __init__(self, session: Session):
        self.session = session

    def create_objet(self, objet: Objet) -> Objet:
        """
        Create a new Objet.

        This method adds a new Objet instance to the database and commits the transaction.

        Parameters:
            objet (Objet): The Objet instance to be created.

        Returns:
            Objet: The created Objet instance with its ID populated.
        """
        self.session.add(objet)
        self.session.commit()
        self.session.refresh(objet)
        return objet

    def get_objet(self, objet_id: int) -> Objet | None:
        """
        Retrieve a Objet by its ID.

        This method fetches a Objet from the database using its unique identifier.

        Parameters:
            objet_id (int): The ID of the Objet to retrieve.

        Returns:
            Objet | None: The Objet instance if found, otherwise None.
        """
        statement = select(Objet).where(Objet.objet_id == objet_id)
        return self.session.exec(statement).one_or_none()

    def get_all_objets(self, limit: int | None = None, offset: int | None = None) -> list[Objet]:
        """
        Retrieve all Objets.

        This method fetches all Objet records from the database.
        
        Parameters:
            limit (int) : an integer to specify the maximum number of results.
            offset (int) : an integer to specify the number of lines to ignore.

        Returns:
            List[Objet]: A list of all Objet instances in the database.
        """
        statement = select(Objet).limit(limit).offset(offset)
        return list(self.session.exec(statement).all())

    def update_objet(self, objet_id: int, objet_update: dict) -> Objet | None:
        """
        Update an existing Objet.

        This method updates the fields of an existing Objet in the database
        with the values from the provided Objet instance.

        Parameters:
            objet_id (int): The ID of the Objet to update.
            objet_update (dict): The dictionary instance containing updated values.

        Returns:
            Objet | None: The updated Objet instance if found, otherwise None.
        """

        existing_objet = self.get_objet(objet_id)
        if existing_objet:
            existing_objet.sqlmodel_update(objet_update)
            self.session.add(existing_objet)
            self.session.commit()
            self.session.refresh(existing_objet)
            return existing_objet
        return None

    def delete_objet(self, objet_id: int) -> bool:
        """
        Delete a Objet by its ID.

        This method removes a Objet from the database using its unique identifier.

        Parameters:
            objet_id (int): The ID of the Objet to delete.

        Returns:
            bool: True if the deletion was successful, otherwise False.
        """
        existing_objet = self.get_objet(objet_id)
        if existing_objet:
            self.session.delete(existing_objet)
            self.session.commit()
            return True
        return False