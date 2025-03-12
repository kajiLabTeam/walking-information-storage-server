from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

from app.utils import timestamp

if TYPE_CHECKING:
    from .building import Building


class Floor(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    level: int = Field(nullable=False)
    name: str = Field(max_length=255, nullable=False)
    building_id: str | None = Field(default=None, foreign_key="buildings.id")
    created_at: datetime | None = Field(default_factory=timestamp)
    updated_at: datetime | None = Field(default_factory=timestamp)
    deleted_at: datetime | None = None

    building: "Building | None" = Relationship(back_populates="floors")
    coordinates: list["Coordinate"] = Relationship(back_populates="floor")


class FloorInformation(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    floor_id: str | None = Field(default=None, foreign_key="floors.id")
    created_at: datetime = Field(default_factory=timestamp)
    updated_at: datetime | None = Field(default_factory=timestamp)
    deleted_at: datetime | None = None


class Coordinate(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    x: int = Field(nullable=False)
    y: int = Field(nullable=False)
    is_walkable: bool = Field(nullable=False)
    floor_id: str | None = Field(default=None, foreign_key="floors.id")
    created_at: datetime | None = Field(default_factory=timestamp)
    updated_at: datetime | None = Field(default_factory=timestamp)
    deleted_at: datetime | None = None

    floor: Floor | None = Relationship(back_populates="coordinates")


class CoordinateInformation(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    coordinate_id: int | None = Field(default=None, foreign_key="coordinates.id")
    created_at: datetime | None = Field(default_factory=timestamp)
    updated_at: datetime | None = Field(default_factory=timestamp)
    deleted_at: datetime | None = None
