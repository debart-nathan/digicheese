from sqlmodel import Session, select
from ..models import DetailCommande

class DetailCommandeRepository:
    """
    Repository class for managing DetailCommande records in the database.

    This class provides methods to perform CRUD (Create, Read, Update, Delete) operations
    on the DetailCommande model. It abstracts the database interactions and provides a clean
    interface for managing DetailCommande records.

    Attributes:
        session (Session): The SQLModel session used for database operations.

    Methods:
        create_detail_commande(detail_commande: DetailCommande) -> DetailCommande:
            Adds a new DetailCommande to the database and returns the created instance.

        get_detail_commande(detail_commande_id: int) -> DetailCommande | None:
            Retrieves a DetailCommande by its ID. Returns None if not found.

        get_all_detail_commandes() -> List[DetailCommande]:
            Fetches all DetailCommande records from the database.

        update_detail_commande(detail_commande: DetailCommande) -> DetailCommande | None:
            Updates an existing DetailCommande with new values. Returns the updated instance
            or None if the DetailCommande was not found.

        delete_detail_commande(detail_commande_id: int) -> bool:
            Deletes a DetailCommande by its ID. Returns True if the deletion was successful,
            or False if the DetailCommande was not found.
    """
        
    def __init__(self, session: Session):
        self.session = session

    def create_detail_commande(self, detail_commande: DetailCommande) -> DetailCommande:
        """
        Create a new DetailCommande.

        This method adds a new DetailCommande instance to the database and commits the transaction.

        Parameters:
            detail_commande (DetailCommande): The DetailCommande instance to be created.

        Returns:
            DetailCommande: The created DetailCommande instance with its ID populated.
        """
        self.session.add(detail_commande)
        self.session.commit()
        self.session.refresh(detail_commande)
        return detail_commande

    def get_detail_commande(self, detail_commande_id: int) -> DetailCommande | None:
        """
        Retrieve a DetailCommande by its ID.

        This method fetches a DetailCommande from the database using its unique identifier.

        Parameters:
            detail_commande_id (int): The ID of the DetailCommande to retrieve.

        Returns:
            DetailCommande | None: The DetailCommande instance if found, otherwise None.
        """
        statement = select(DetailCommande).where(DetailCommande.detail_commande_id == detail_commande_id)
        return self.session.exec(statement).one_or_none()

    def get_all_detail_commandes(self,limit: int | None = None, offset: int | None = None ) -> list[DetailCommande]:
        """
        Retrieve all DetailCommandes.

        This method fetches all DetailCommande records from the database.

        Returns:
            List[DetailCommande]: A list of all DetailCommande instances in the database.
        """
        statement = select(DetailCommande).limit(limit).offset(offset)
        return list(self.session.exec(statement).all())

    def update_detail_commande(self, detail_commande_id: int ,detail_commande_update: dict) -> DetailCommande | None:
        """
        Update an existing DetailCommande.

        This method updates the fields of an existing DetailCommande in the database
        with the values from the provided DetailCommande instance.

        Parameters:
            detail_commande (DetailCommande): The DetailCommande instance containing updated values.

        Returns:
            DetailCommande | None: The updated DetailCommande instance if found, otherwise None.
        """

        existing_detail_commande = self.get_detail_commande(detail_commande_id)
        if existing_detail_commande:
            existing_detail_commande.sqlmodel_update(detail_commande_update)
            self.session.add(existing_detail_commande)
            self.session.commit()
            self.session.refresh(existing_detail_commande)
            return existing_detail_commande
        return None

    def delete_detail_commande(self, detail_commande_id: int) -> bool:
        """
        Delete a DetailCommande by its ID.

        This method removes a DetailCommande from the database using its unique identifier.

        Parameters:
            detail_commande_id (int): The ID of the DetailCommande to delete.

        Returns:
            bool: True if the deletion was successful, otherwise False.
        """
        existing_detail_commande = self.get_detail_commande(detail_commande_id)
        if existing_detail_commande:
            self.session.delete(existing_detail_commande)
            self.session.commit()
            return True
        return False