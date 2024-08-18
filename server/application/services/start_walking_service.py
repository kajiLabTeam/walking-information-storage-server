from domain.repository_impl.trajectory_repository_impl import TrajectoryRepositoryImpl
from infrastructure.connection import DBConnection


class StartWalkingService:
    def __init__(
        self,
        trajectory_repo: TrajectoryRepositoryImpl,
    ):
        self.__trajectory_repo = trajectory_repo

    def run(self, pedestrian_id: str, floor_id: str) -> str:
        conn = DBConnection.connect()

        trajectory_id = self.__trajectory_repo.save(
            conn=conn, is_walking=True, floor_id=floor_id
        )

        return trajectory_id
