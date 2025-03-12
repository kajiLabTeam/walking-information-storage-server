from sqlmodel import Session, select

from app.infrastructure.persistence.models import CorrectPosition, EstimatedPosition, Trajectory


class TrajectoryRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, trajectory: Trajectory) -> Trajectory:
        self.session.add(trajectory)
        self.session.commit()
        return trajectory


class CorrectPositionRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, correct_position: CorrectPosition) -> CorrectPosition:
        self.session.add(correct_position)
        self.session.commit()
        return correct_position

    def get_by_trajectory_id(self, trajectory_id: str) -> list[CorrectPosition]:
        statement = select(CorrectPosition).where(CorrectPosition.trajectory_id == trajectory_id)
        return list(self.session.exec(statement).all())


class EstimatedPositionRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, estimated_position: EstimatedPosition) -> EstimatedPosition:
        self.session.add(estimated_position)
        self.session.commit()
        return estimated_position

    def get_by_trajectory_id(self, trajectory_id: str) -> list[EstimatedPosition]:
        statement = select(EstimatedPosition).where(
            EstimatedPosition.trajectory_id == trajectory_id
        )
        return list(self.session.exec(statement).all())
