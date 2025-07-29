from sqlmodel import Session, select
from ..models import VariationObjet

class VariationObjetRepository:
    """
    Repository class for managing VariationObjet records in the database.

    This class provides methods to perform CRUD (Create, Read, Update, Delete) operations
    on the VariationObjet model. It abstracts the database interactions and provides a clean
    interface for managing VariationObjet records.

    Attributes:
        session (Session): The SQLModel session used for database operations.

    Methods:
        create_variation_objet(client: VariationObjet) -> VariationObjet:
            Adds a new VariationObjet to the database and returns the created instance.

        get_variation_objet(variation_objet_id: int) -> VariationObjet | None:
            Retrieves a VariationObjet by its ID. Returns None if not found.

        get_all_variation_objets(limit: int | None = None, offset: int | None = None) -> List[VariationObjet]:
            Fetches all VariationObjet records from the database.

        update_variation_objet(variation_objet_id: int, variation_objet_update: dict) -> VariationObjet | None:
            Updates an existing VariationObjet with new values. Returns the updated instance
            or None if the VariationObjet was not found.

        delete_variation_objet(variation_objet_id: int) -> bool:
            Deletes a VariationObjet by its ID. Returns True if the deletion was successful,
            or False if the VariationObjet was not found.
    """     
    def __init__(self, session: Session):
        self.session = session

    def create_variation_objet(self, variation_objet: VariationObjet) -> VariationObjet:
        """
        Create a new VariationObjet.

        This method adds a new VariationObjet instance to the database and commits the transaction.

        Parameters:
            variation_objet (VariationObjet): The VariationObjet instance to be created.

        Returns:
            VariationObjet: The created VariationObjet instance with its ID populated.
        """
        self.session.add(variation_objet)
        self.session.commit()
        self.session.refresh(variation_objet)
        return variation_objet

    def get_variation_objet(self, variation_objet_id: int) -> VariationObjet | None:
        """
        Retrieve a VariationObjet by its ID.

        This method fetches a VariationObjet from the database using its unique identifier.

        Parameters:
            variation_objet_id (int): The ID of the VariationObjet to retrieve.

        Returns:
            VariationObjet | None: The VariationObjet instance if found, otherwise None.
        """
        statement = select(VariationObjet).where(VariationObjet.variation_objet_id == variation_objet_id)
        return self.session.exec(statement).one_or_none()

    def get_all_variation_objets(self, limit: int | None = None, offset: int | None = None) -> list[VariationObjet]:
        """
        Retrieve all VariationObjets.

        This method fetches all VariationObjet records from the database.

        Parameters:
            limit (int) : an integer to specify the maximum number of results.
            offset (int) : an integer to specify the number of lines to ignore.

        Returns:
            List[VariationObjet]: A list of all VariationObjet instances in the database.
        """
        statement = select(VariationObjet).limit(limit).offset(offset)
        return list(self.session.exec(statement).all())

    def update_variation_objet(self, variation_objet_id: int, variation_objet_update: dict) -> VariationObjet | None:
        """
        Update an existing VariationObjet.

        This method updates the fields of an existing VariationObjet in the database
        with the values from the provided VariationObjet instance.

        Parameters:
            variation_objet_id (int): The ID of the VariationObjet to update.
            variation_objet_update (dict): The dictionary instance containing updated values.

        Returns:
            VariationObjet | None: The updated VariationObjet instance if found, otherwise None.
        """
        existing_variation_objet = self.get_variation_objet(variation_objet_id)
        if existing_variation_objet:
            existing_variation_objet.sqlmodel_update(variation_objet_update)
            self.session.add(existing_variation_objet)
            self.session.commit()
            self.session.refresh(existing_variation_objet)
            return existing_variation_objet
        return None

    def delete_variation_objet(self, variation_objet_id: int) -> bool:
        """
        Delete a VariationObjet by its ID.

        This method removes a VariationObjet from the database using its unique identifier.

        Parameters:
            variation_objet_id (int): The ID of the VariationObjet to delete.

        Returns:
            bool: True if the deletion was successful, otherwise False.
        """
        existing_variation_objet = self.get_variation_objet(variation_objet_id)
        if existing_variation_objet:
            self.session.delete(existing_variation_objet)
            self.session.commit()
            return True
        return False