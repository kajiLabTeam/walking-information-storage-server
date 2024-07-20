from domain.repository_impl.trajectory_repository_impl import (
    RealtimeTrajectoryRepositoryImpl, TrajectoryRepositoryImpl)
from infrastructure.connection import DBConnection


class StartWalkingService:
    def __init__(
        self,
        trajectory_repo: TrajectoryRepositoryImpl,
        realtime_trajectory_repo: RealtimeTrajectoryRepositoryImpl,
    ):
        self.__trajectory_repo = trajectory_repo
        self.__realtime_trajectory_repo = realtime_trajectory_repo

    def run(self, pedestrian_id: str, floor_map_id: str) -> str:
        conn = DBConnection.connect()

        trajectory_id = self.__trajectory_repo.save(
            conn=conn, pedestrian_id=pedestrian_id, floor_map_id=floor_map_id
        )

        self.__realtime_trajectory_repo.save(conn=conn, trajectory_id=trajectory_id)

        return trajectory_id
