from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

from app.utils import timestamp

if TYPE_CHECKING:
    from app.infrastructure.persistence.models import EstimatedPosition, Trajectory


class Pedestrian(SQLModel, table=True):
    __tablename__: str = "pedestrians"  # type: ignore  # noqa: PGH003

    id: str = Field(default=None, primary_key=True)
    created_at: datetime | None = Field(default_factory=timestamp)
    updated_at: datetime | None = Field(default_factory=timestamp)
    deleted_at: datetime | None = None

    trajectories: list["Trajectory"] = Relationship(back_populates="pedestrian")
    walking_information: list["WalkingInformation"] = Relationship(back_populates="pedestrian")


class WalkingInformation(SQLModel, table=True):
    __tablename__: str = "walking_information"  # type: ignore  # noqa: PGH003

    id: str = Field(default=None, primary_key=True)
    created_at: datetime | None = Field(default_factory=timestamp)
    updated_at: datetime | None = Field(default_factory=timestamp)
    deleted_at: datetime | None = None

    pedestrian_id: str = Field(foreign_key="pedestrians.id")
    pedestrian: Optional["Pedestrian"] = Relationship(back_populates="walking_information")

    estimated_positions: list["EstimatedPosition"] = Relationship(
        back_populates="walking_information"
    )
