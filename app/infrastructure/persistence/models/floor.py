from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

from app.utils import timestamp

if TYPE_CHECKING:
    from app.infrastructure.persistence.models import Building, Trajectory


class Floor(SQLModel, table=True):
    __tablename__: str = "floors"  # type: ignore  # noqa: PGH003

    id: str = Field(default=None, primary_key=True)
    level: int = Field(nullable=False)
    name: str = Field(max_length=255, nullable=False)
    created_at: datetime | None = Field(default_factory=timestamp)
    updated_at: datetime | None = Field(default_factory=timestamp)
    deleted_at: datetime | None = None

    building_id: str | None = Field(default=None, foreign_key="buildings.id")
    building: Optional["Building"] = Relationship(back_populates="floors")

    coordinates: list["Coordinate"] = Relationship(back_populates="floor")
    trajectories: list["Trajectory"] = Relationship(back_populates="floor")
    floor_information: list["FloorInformation"] = Relationship(back_populates="floor")


class FloorInformation(SQLModel, table=True):
    __tablename__: str = "floor_information"  # type: ignore  # noqa: PGH003

    id: str = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=timestamp)
    updated_at: datetime | None = Field(default_factory=timestamp)
    deleted_at: datetime | None = None

    floor_id: str | None = Field(default=None, foreign_key="floors.id")
    floor: Optional["Floor"] = Relationship(back_populates="floor_information")


class Coordinate(SQLModel, table=True):
    __tablename__: str = "coordinates"  # type: ignore  # noqa: PGH003

    id: int = Field(default=None, primary_key=True)
    x: int = Field(nullable=False)
    y: int = Field(nullable=False)
    is_walkable: bool = Field(nullable=False)
    created_at: datetime | None = Field(default_factory=timestamp)
    updated_at: datetime | None = Field(default_factory=timestamp)
    deleted_at: datetime | None = None

    floor_id: str | None = Field(default=None, foreign_key="floors.id")
    floor: Floor | None = Relationship(back_populates="coordinates")

    coordinate_information: list["CoordinateInformation"] = Relationship(
        back_populates="coordinate"
    )


class CoordinateInformation(SQLModel, table=True):
    __tablename__: str = "coordinate_information"  # type: ignore  # noqa: PGH003

    id: str = Field(default=None, primary_key=True)
    created_at: datetime | None = Field(default_factory=timestamp)
    updated_at: datetime | None = Field(default_factory=timestamp)
    deleted_at: datetime | None = None

    coordinate_id: int | None = Field(default=None, foreign_key="coordinates.id")
    coordinate: Optional["Coordinate"] = Relationship(back_populates="coordinate_information")
