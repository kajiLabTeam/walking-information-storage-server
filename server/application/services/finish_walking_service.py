from server.application.dto import FinishWalkingServiceDto
from server.domain.repository_impl import TrajectoryRepositoryImpl
from server.infrastructure.connection import DBConnection


class FinishWalkingService:
    def __init__(
        self,
        trajectory_repo: TrajectoryRepositoryImpl,
    ) -> None:
        self.__trajectory_repo = trajectory_repo

    def run(
        self,
        trajectory_id: str,
    ) -> FinishWalkingServiceDto:
        conn = DBConnection.connect()

        self.__trajectory_repo.update(
            conn=conn,
            is_walking=False,
            trajectory_id=trajectory_id,
        )

        return FinishWalkingServiceDto(trajectory_id=trajectory_id)
