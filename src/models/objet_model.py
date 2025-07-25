from sqlmodel import SQLModel, Field, Relationship

class ObjetBase(SQLModel):
    objet_libelee: str | None = Field(default=None, max_length=50, nullable=True)
    objet_points: int| None = Field(default=0, nullable=False)

class Objet(ObjetBase, table=True):
    __tablename__ = "t_objets"
    objet_id: int | None = Field(default=None, primary_key=True)
    variations_objet: list["VariationObjet"] = Relationship(back_populates="objet")


class ObjetCreate(ObjetBase):
    pass

class ObjetUpdate(ObjetBase):
    objet_points: int | None = Field(default=0,nullable=True)

class ObjetRead(ObjetBase):
    objet_id: int | None = Field(default=None, primary_key=True)