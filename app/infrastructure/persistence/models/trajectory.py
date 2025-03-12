from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

from app.utils import timestamp

if TYPE_CHECKING:
    from .pedestrian import Pedestrian


class Trajectory(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    is_walking: bool = Field(nullable=False)
    pedestrian_id: str = Field(foreign_key="pedestrians.id")
    floor_id: str = Field(foreign_key="floors.id")
    created_at: datetime | None = Field(default_factory=timestamp)
    updated_at: datetime | None = Field(default_factory=timestamp)
    deleted_at: datetime | None = None

    pedestrian: "Pedestrian | None" = Relationship(back_populates="trajectories")


class CorrectPosition(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    x: int = Field(nullable=False)
    y: int = Field(nullable=False)
    direction: int = Field(nullable=False)
    trajectory_id: str = Field(foreign_key="trajectories.id")
    created_at: datetime | None = Field(default_factory=timestamp)
    updated_at: datetime | None = Field(default_factory=timestamp)
    deleted_at: datetime | None = None


class EstimatedPosition(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    x: int = Field(nullable=False)
    y: int = Field(nullable=False)
    is_converged: bool = Field(nullable=False)
    direction: int = Field(nullable=False)
    trajectory_id: str = Field(foreign_key="trajectories.id")
    walking_information_id: str = Field(foreign_key="walking_information.id")
    created_at: datetime | None = Field(default_factory=timestamp)
    updated_at: datetime | None = Field(default_factory=timestamp)
    deleted_at: datetime | None = None
