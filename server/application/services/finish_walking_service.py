from domain.repository_impl.trajectory_repository_impl import \
    TrajectoryRepositoryImpl
from infrastructure.connection import DBConnection


class FinishWalkingService:
    def __init__(
        self,
        trajectory_repo: TrajectoryRepositoryImpl,
    ):
        self.__trajectory_repo = trajectory_repo

    def run(self, trajectory_id: str) -> str:
        conn = DBConnection.connect()

        self.__trajectory_repo.update(conn=conn, trajectory_id=trajectory_id)

        return trajectory_id
