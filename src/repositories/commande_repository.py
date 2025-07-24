from sqlmodel import Session, select
from ..models import Commande

class CommandeRepository:
    """
    Repository class for managing Commande records in the database.

    This class provides methods to perform CRUD (Create, Read, Update, Delete) operations
    on the Commande model. It abstracts the database interactions and provides a clean
    interface for managing Commande records.

    Attributes:
        session (Session): The SQLModel session used for database operations.

    Methods:
        create_commande(commande: Commande) -> Commande:
            Adds a new Commande to the database and returns the created instance.

        get_commande(commande_id: int) -> Commande | None:
            Retrieves a Commande by its ID. Returns None if not found.

        get_all_commandes() -> List[Commande]:
            Fetches all Commande records from the database.

        update_commande(commande: Commande) -> Commande | None:
            Updates an existing Commande with new values. Returns the updated instance
            or None if the Commande was not found.

        delete_commande(commande_id: int) -> bool:
            Deletes a Commande by its ID. Returns True if the deletion was successful,
            or False if the Commande was not found.
    """
        
    def __init__(self, session: Session):
        self.session = session

    def create_commande(self, commande: Commande) -> Commande:
        """
        Create a new Commande.

        This method adds a new Commande instance to the database and commits the transaction.

        Parameters:
            commande (Commande): The Commande instance to be created.

        Returns:
            Commande: The created Commande instance with its ID populated.
        """
        self.session.add(commande)
        self.session.commit()
        self.session.refresh(commande)
        return commande

    def get_commande(self, commande_id: int) -> Commande | None:
        """
        Retrieve a Commande by its ID.

        This method fetches a Commande from the database using its unique identifier.

        Parameters:
            commande_id (int): The ID of the Commande to retrieve.

        Returns:
            Commande | None: The Commande instance if found, otherwise None.
        """
        statement = select(Commande).where(Commande.commande_id == commande_id)
        return self.session.exec(statement).one_or_none()

    def get_all_commandes(self,limit: int | None = None, offset: int | None = None ) -> list[Commande]:
        """
        Retrieve all Commandes.

        This method fetches all Commande records from the database.

        Returns:
            List[Commande]: A list of all Commande instances in the database.
        """
        statement = select(Commande).limit(limit).offset(offset)
        return list(self.session.exec(statement).all())

    def update_commande(self, commande_id: int ,commande_update: dict) -> Commande | None:
        """
        Update an existing Commande.

        This method updates the fields of an existing Commande in the database
        with the values from the provided Commande instance.

        Parameters:
            commande (Commande): The Commande instance containing updated values.

        Returns:
            Commande | None: The updated Commande instance if found, otherwise None.
        """

        existing_commande = self.get_commande(commande_id)
        if existing_commande:
            existing_commande.sqlmodel_update(commande_update)
            self.session.add(existing_commande)
            self.session.commit()
            self.session.refresh(existing_commande)
            return existing_commande
        return None

    def delete_commande(self, commande_id: int) -> bool:
        """
        Delete a Commande by its ID.

        This method removes a Commande from the database using its unique identifier.

        Parameters:
            commande_id (int): The ID of the Commande to delete.

        Returns:
            bool: True if the deletion was successful, otherwise False.
        """
        existing_commande = self.get_commande(commande_id)
        if existing_commande:
            self.session.delete(existing_commande)
            self.session.commit()
            return True
        return False