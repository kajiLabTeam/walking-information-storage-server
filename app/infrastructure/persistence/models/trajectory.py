from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

from app.utils import timestamp

if TYPE_CHECKING:
    from app.infrastructure.persistence.models import Floor, Pedestrian, WalkingInformation


class Trajectory(SQLModel, table=True):
    __tablename__: str = "trajectories"  # type: ignore  # noqa: PGH003

    id: str = Field(default=None, primary_key=True)
    is_walking: bool = Field(nullable=False)
    created_at: datetime | None = Field(default_factory=timestamp)
    updated_at: datetime | None = Field(default_factory=timestamp)
    deleted_at: datetime | None = None

    floor_id: str = Field(foreign_key="floors.id")
    floor: Optional["Floor"] = Relationship(back_populates="trajectories")

    pedestrian_id: str = Field(foreign_key="pedestrians.id")
    pedestrian: Optional["Pedestrian"] = Relationship(back_populates="trajectories")

    correct_positions: list["CorrectPosition"] = Relationship(back_populates="trajectory")
    estimated_positions: list["EstimatedPosition"] = Relationship(back_populates="trajectory")


class CorrectPosition(SQLModel, table=True):
    __tablename__: str = "correct_positions"  # type: ignore  # noqa: PGH003

    id: str = Field(default=None, primary_key=True)
    x: int = Field(nullable=False)
    y: int = Field(nullable=False)
    direction: int = Field(nullable=False)
    created_at: datetime | None = Field(default_factory=timestamp)
    updated_at: datetime | None = Field(default_factory=timestamp)
    deleted_at: datetime | None = None

    trajectory_id: str = Field(foreign_key="trajectories.id")
    trajectory: Optional["Trajectory"] = Relationship(back_populates="correct_positions")


class EstimatedPosition(SQLModel, table=True):
    __tablename__: str = "estimated_positions"  # type: ignore  # noqa: PGH003

    id: str = Field(default=None, primary_key=True)
    x: int = Field(nullable=False)
    y: int = Field(nullable=False)
    is_converged: bool = Field(nullable=False)
    direction: int = Field(nullable=False)
    created_at: datetime | None = Field(default_factory=timestamp)
    updated_at: datetime | None = Field(default_factory=timestamp)
    deleted_at: datetime | None = None

    trajectory_id: str = Field(foreign_key="trajectories.id")
    trajectory: Optional["Trajectory"] = Relationship(back_populates="estimated_positions")

    walking_information_id: str = Field(foreign_key="walking_information.id")
    walking_information: Optional["WalkingInformation"] = Relationship(
        back_populates="estimated_positions"
    )
