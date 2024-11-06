from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional
from ..db import db

class Cat(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    color: Mapped[str]
    personality: Mapped[str]
    caretaker_id: Mapped[Optional[int]] = mapped_column(ForeignKey("caretaker.id"))
    caretaker: Mapped[Optional["Caretaker"]] = relationship(back_populates="cats")

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            color=self.color,
            personality=self.personality,
            caretaker=self.caretaker.name if self.caretaker else None
        )
    
    @classmethod
    def from_dict(cls, cat_data):
        return cls(
            name=cat_data["name"],
            color=cat_data["color"],
            personality=cat_data["personality"],
            caretaker_id=cat_data.get("caretaker_id", None) 
        )