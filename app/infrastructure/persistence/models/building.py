from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

from app.utils import timestamp

if TYPE_CHECKING:
    from app.infrastructure.persistence.models import Floor


class Building(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    name: str = Field(max_length=255, nullable=False)
    latitude: float = Field(nullable=False)
    longitude: float = Field(nullable=False)
    created_at: datetime | None = Field(default_factory=timestamp)
    updated_at: datetime | None = Field(default_factory=timestamp)
    deleted_at: datetime | None = None

    floors: list["Floor"] = Relationship(back_populates="building")
