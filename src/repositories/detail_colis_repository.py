from sqlmodel import Session, select
from ..models import DetailColis

class DetailColisRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_DetailColis(self, DetailColis: DetailColis) -> DetailColis:
        self.session.add(DetailColis)
        self.session.commit()
        self.session.refresh(DetailColis)
        return DetailColis

    def get_DetailColis(self, DetailColis_id: int) -> DetailColis | None:
        statement = select(DetailColis).where(DetailColis.DetailColis_id == DetailColis_id)
        return self.session.exec(statement).one_or_none()

    def get_all_DetailColiss(self,limit: int | None = None, offset: int | None = None ) -> list[DetailColis]:
        statement = select(DetailColis).limit(limit).offset(offset)
        return list(self.session.exec(statement).all())

    def update_DetailColis(self, DetailColis_id: int ,DetailColis_update: dict) -> DetailColis | None:
        existing_DetailColis = self.get_DetailColis(DetailColis_id)
        if existing_DetailColis:
            existing_DetailColis.sqlmodel_update(DetailColis_update)
            self.session.add(existing_DetailColis)
            self.session.commit()
            self.session.refresh(existing_DetailColis)
            return existing_DetailColis
        return None

    def delete_DetailColis(self, DetailColis_id: int) -> bool:
        existing_DetailColis = self.get_DetailColis(DetailColis_id)
        if existing_DetailColis:
            self.session.delete(existing_DetailColis)
            self.session.commit()
            return True
        return False