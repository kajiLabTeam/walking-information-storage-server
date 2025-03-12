from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

from app.utils import timestamp

if TYPE_CHECKING:
    from .trajectory import Trajectory


class Pedestrian(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    created_at: datetime | None = Field(default_factory=timestamp)
    updated_at: datetime | None = Field(default_factory=timestamp)
    deleted_at: datetime | None = None

    trajectories: list["Trajectory"] = Relationship(back_populates="pedestrian")


class WalkingInformation(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    pedestrian_id: str = Field(foreign_key="pedestrians.id")
    created_at: datetime | None = Field(default_factory=timestamp)
    updated_at: datetime | None = Field(default_factory=timestamp)
    deleted_at: datetime | None = None

    pedestrian: Pedestrian | None = Relationship(back_populates="walking_information")
