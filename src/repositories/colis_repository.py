from sqlmodel import Session, select
from ..models import Colis

class ColisRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_Colis(self, Colis: Colis) -> Colis:
        self.session.add(Colis)
        self.session.commit()
        self.session.refresh(Colis)
        return Colis

    def get_Colis(self, Colis_id: int) -> Colis | None:
        statement = select(Colis).where(Colis.Colis_id == Colis_id)
        return self.session.exec(statement).one_or_none()

    def get_all_Coliss(self,limit: int | None = None, offset: int | None = None ) -> list[Colis]:
        statement = select(Colis).limit(limit).offset(offset)
        return list(self.session.exec(statement).all())

    def update_Colis(self, Colis_id: int ,Colis_update: dict) -> Colis | None:
        existing_Colis = self.get_Colis(Colis_id)
        if existing_Colis:
            existing_Colis.sqlmodel_update(Colis_update)
            self.session.add(existing_Colis)
            self.session.commit()
            self.session.refresh(existing_Colis)
            return existing_Colis
        return None

    def delete_Colis(self, Colis_id: int) -> bool:
        existing_Colis = self.get_Colis(Colis_id)
        if existing_Colis:
            self.session.delete(existing_Colis)
            self.session.commit()
            return True
        return False