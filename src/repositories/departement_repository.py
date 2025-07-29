from sqlmodel import Session, select
from ..models import Departement

class DepartementRepository:
    """
    Repository class for managing Departement records in the database.

    This class provides methods to perform CRUD (Create, Read, Update, Delete) operations
    on the Departement model. It abstracts the database interactions and provides a clean
    interface for managing Departement records.

    Attributes:
        session (Session): The SQLModel session used for database operations.

    Methods:
        create_departement(departement: Departement) -> Departement:
            Adds a new Departement to the database and returns the created instance.

        get_departement(departement_code: int) -> Departement | None:
            Retrieves a Departement by its ID. Returns None if not found.

        get_all_departement(limit: int | None = None, offset: int | None = None) -> List[Departement]:
            Fetches all Departement records from the database.

        update_departement(departement_code: int, departement_update: dict) -> Departement | None:
            Updates an existing Departement with new values. Returns the updated instance
            or None if the Departement was not found.

        delete_departement(departement_code: int) -> bool:
            Deletes a Departement by its ID. Returns True if the deletion was successful,
            or False if the Departement was not found.
    """      
    def __init__(self, session: Session):
        self.session = session

    def create_departement(self, departement: Departement) -> Departement:
        """
        Create a new Departement.

        This method adds a new Departement instance to the database and commits the transaction.

        Parameters:
            departement (Departement): The Departement instance to be created.

        Returns:
            Departement: The created Departement instance with its ID populated.
        """
        self.session.add(departement)
        self.session.commit()
        self.session.refresh(departement)
        return departement

    def get_departement(self, departement_code: int) -> Departement | None:
        """
        Retrieve a Departement by its ID.

        This method fetches a Departement from the database using its unique identifier.

        Parameters:
            departement_code (int): The ID of the Departement to retrieve.

        Returns:
            Departement | None: The Departement instance if found, otherwise None.
        """
        statement = select(Departement).where(Departement.departement_code == departement_code)
        return self.session.exec(statement).one_or_none()

    def get_all_departement(self, limit: int | None = None, offset: int | None = None) -> list[Departement]:
        """
        Retrieve all Departements.

        This method fetches all Departement records from the database.

        Parameters:
            limit (int) : an integer to specify the maximum number of results.
            offset (int) : an integer to specify the number of lines to ignore.

        Returns:
            List[Departement]: A list of all Departement instances in the database.
        """
    
        statement = select(Departement).limit(limit).offset(offset)
        return list(self.session.exec(statement).all())

    def update_departement(self, departement_code: int, departement_update: dict) -> Departement | None:
        """
        Update an existing Departement.

        This method updates the fields of an existing Departement in the database
        with the values from the provided Departement instance.

        Parameters:
            departement_code (int): The ID of the Departement to update.
            departement_update (dict): The dictionary instance containing updated values.

        Returns:
            Departement | None: The updated Departement instance if found, otherwise None.
        """
        existing_departement = self.get_departement(departement_code)
        if existing_departement:
            existing_departement.sqlmodel_update(departement_update)
            self.session.add(existing_departement)
            self.session.commit()
            self.session.refresh(existing_departement)
            return existing_departement
        return None

    def delete_departement(self, departement_code: int) -> bool:
        """
        Delete a Departement by its ID.

        This method removes a Departement from the database using its unique identifier.

        Parameters:
            departement_code (int): The ID of the Departement to delete.

        Returns:
            bool: True if the deletion was successful, otherwise False.
        """
        existing_departement = self.get_departement(departement_code)
        if existing_departement:
            self.session.delete(existing_departement)
            self.session.commit()
            return True
        return False