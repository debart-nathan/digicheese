from sqlmodel import Session, select
from ..models import DetailColis

class DetailColisRepository:
    """
    Repository class for managing DetailColis records in the database.

    This class provides methods to perform CRUD (Create, Read, Update, Delete) operations
    on the DetailColis model. It abstracts the database interactions and provides a clean
    interface for managing DetailColis records.

    Attributes:
        session (Session): The SQLModel session used for database operations.

    Methods:
        create_detail_colis(detail_colis: DetailColis) -> DetailColis:
            Adds a new DetailColis to the database and returns the created instance.

        get_detail_colis(detail_colis_id: int) -> DetailColis | None:
            Retrieves a DetailColis by its ID. Returns None if not found.

        get_all_detail_colis(imit: int | None = None, offset: int | None = None) -> List[DetailColis]:
            Fetches all DetailColis records from the database.

        update_detail_colis(ddetail_colis_id: int, detail_colis_update: dict) -> DetailColis | None:
            Updates an existing DetailColis with new values. Returns the updated instance
            or None if the DetailColis was not found.

        delete_detail_colis(detail_colis_id: int) -> bool:
            Deletes a DetailColis by its ID. Returns True if the deletion was successful,
            or False if the DetailColis was not found.
    """
        
    def __init__(self, session: Session):
        self.session = session

    def create_detail_colis(self, detail_colis: DetailColis) -> DetailColis:
        """
        Create a new DetailColis.

        This method adds a new DetailColis instance to the database and commits the transaction.

        Parameters:
            detail_colis (DetailColis): The DetailColis instance to be created.

        Returns:
            DetailColis: The created DetailColis instance with its ID populated.
        """
        self.session.add(detail_colis)
        self.session.commit()
        self.session.refresh(detail_colis)
        return detail_colis

    def get_detail_colis(self, detail_colis_id: int) -> DetailColis | None:
        """
        Retrieve a DetailColis by its ID.

        This method fetches a DetailColis from the database using its unique identifier.

        Parameters:
            detail_colis_id (int): The ID of the DetailColis to retrieve.

        Returns:
            DetailColis | None: The DetailColis instance if found, otherwise None.
        """
        statement = select(DetailColis).where(DetailColis.detail_colis_id == detail_colis_id)
        return self.session.exec(statement).one_or_none()

    def get_all_detail_colis(self, limit: int | None = None, offset: int | None = None) -> list[DetailColis]:
        """
        Retrieve all DetailColiss.

        This method fetches all DetailColis records from the database.

        Parameters:
            limit (int) : an integer to specify the maximum number of results.
            offset (int) : an integer to specify the number of lines to ignore.


        Returns:
            List[DetailColis]: A list of all DetailColis instances in the database.
        """
        statement = select(DetailColis).limit(limit).offset(offset)
        return list(self.session.exec(statement).all())

    def update_detail_colis(self, detail_colis_id: int, detail_colis_update: dict) -> DetailColis | None:
        """
        Update an existing DetailColis.

        This method updates the fields of an existing DetailColis in the database
        with the values from the provided DetailColis instance.

        Parameters:
            detail_colis_id (int): The ID of the DetailColis to update.
            detail_colis_update (dict): The dictionary instance containing updated values.

        Returns:
            DetailColis | None: The updated DetailColis instance if found, otherwise None.
        """

        existing_detail_colis = self.get_detail_colis(detail_colis_id)
        if existing_detail_colis:
            existing_detail_colis.sqlmodel_update(detail_colis_update)
            self.session.add(existing_detail_colis)
            self.session.commit()
            self.session.refresh(existing_detail_colis)
            return existing_detail_colis
        return None

    def delete_detail_colis(self, detail_colis_id: int) -> bool:
        """
        Delete a DetailColis by its ID.

        This method removes a DetailColis from the database using its unique identifier.

        Parameters:
            detail_colis_id (int): The ID of the DetailColis to delete.

        Returns:
            bool: True if the deletion was successful, otherwise False.
        """
        existing_detail_colis = self.get_detail_colis(detail_colis_id)
        if existing_detail_colis:
            self.session.delete(existing_detail_colis)
            self.session.commit()
            return True
        return False