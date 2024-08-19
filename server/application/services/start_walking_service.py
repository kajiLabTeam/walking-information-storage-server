from application.dto.application_dto import StartWalkingServiceDto
from application.errors.application_error import ApplicationError, ApplicationErrorType
from domain.repository_impl.floor_repository_impl import FloorInformationRepositoryImpl
from domain.repository_impl.trajectory_repository_impl import TrajectoryRepositoryImpl
from infrastructure.connection import DBConnection


class StartWalkingService:
    def __init__(
        self,
        trajectory_repo: TrajectoryRepositoryImpl,
        floor_information_repo: FloorInformationRepositoryImpl,
    ):
        self.__trajectory_repo = trajectory_repo
        self.__floor_information_repo = floor_information_repo

    def run(self, pedestrian_id: str, floor_id: str) -> StartWalkingServiceDto:
        conn = DBConnection.connect()

        floor_information_id = self.__floor_information_repo.find_latest(conn=conn)
        if floor_information_id is None:
            raise ApplicationError(
                error_type=ApplicationErrorType.NOT_FLOOR_INFORMATION,
                message="The floor information is not found.",
            )

        trajectory_id = self.__trajectory_repo.save(
            conn=conn,
            is_walking=True,
            pedestrian_id=pedestrian_id,
            floor_information_id=floor_information_id,
        )

        return StartWalkingServiceDto(
            trajectory_id=trajectory_id, floor_information_id=floor_information_id
        )
