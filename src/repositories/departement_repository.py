from sqlmodel import Session, select
from ..models import Departement

class DepartementRepository:   
    def __init__(self, session: Session):
        self.session = session

    def create_departement(self, departement: Departement) -> Departement:
        self.session.add(departement)
        self.session.commit()
        self.session.refresh(departement)
        return departement

    def get_departement(self, departement_code: int) -> Departement | None:
        statement = select(Departement).where(Departement.departement_code == departement_code)
        return self.session.exec(statement).one_or_none()

    def get_all_departement(self,limit: int | None = None, offset: int | None = None ) -> list[Departement]:
        statement = select(Departement).limit(limit).offset(offset)
        return list(self.session.exec(statement).all())

    def update_departement(self, departement_code: int ,departement_update: dict) -> Departement | None:
        existing_departement = self.get_departement(departement_code)
        if existing_departement:
            existing_departement.sqlmodel_update(departement_update)
            self.session.add(existing_departement)
            self.session.commit()
            self.session.refresh(existing_departement)
            return existing_departement
        return None

    def delete_departement(self, departement_code: int) -> bool:
        existing_departement = self.get_departement(departement_code)
        if existing_departement:
            self.session.delete(existing_departement)
            self.session.commit()
            return True
        return False