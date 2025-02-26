from server.application.dto import GenerateTrajectoryServiceDto
from server.domain.repository_impl import (
    CorrectPositionRepositoryImpl,
    EstimatedPositionRepositoryImpl,
    FloorInformationRepositoryImpl,
    TrajectoryRepositoryImpl,
    WalkingInformationRepositoryImpl,
)
from server.infrastructure.connection import DBConnection, MinIOConnection
from server.infrastructure.external.services import FileService
from server.utils import (
    get_accelerometer_bucket_name,
    get_atmospheric_pressure_bucket_name,
    get_gps_bucket_name,
    get_gyroscope_bucket_name,
    get_ratio_wave_bucket_name,
)


class GenerateTrajectoryService:
    def __init__(
        self,
        trajectory_repo: TrajectoryRepositoryImpl,
        estimated_position_repo: EstimatedPositionRepositoryImpl,
        correct_position_repo: CorrectPositionRepositoryImpl,
        floor_information_repo: FloorInformationRepositoryImpl,
        walking_information_repo: WalkingInformationRepositoryImpl,
    ) -> None:
        self.__trajectory_repo = trajectory_repo
        self.__estimated_position_repo = estimated_position_repo
        self.__correct_position_repo = correct_position_repo
        self.__floor_information_repo = floor_information_repo
        self.__walking_information_repo = walking_information_repo

    def run(
        self,
        pedestrian_id: str,
        trajectory_id: str,
        floor_information_id: str,
        gps_file: bytes,
        wifi_file: bytes,
        gyroscope_file: bytes,
        accelerometer_file: bytes,
        atmospheric_pressure_file: bytes,
    ) -> GenerateTrajectoryServiceDto:
        conn = DBConnection.connect()
        s3 = MinIOConnection.connect()
        file_service = FileService(s3)

        # walking_informationテーブルにデータを保存
        walking_information_dto = self.__walking_information_repo.save(
            conn=conn, pedestrian_id=pedestrian_id
        )

        # センサデータMinIOに保存
        key_file: list[tuple[str, bytes]] = [
            (get_gps_bucket_name(walking_information_dto.id), gps_file),
            (get_ratio_wave_bucket_name(walking_information_dto.id), wifi_file),
            (get_gyroscope_bucket_name(walking_information_dto.id), gyroscope_file),
            (get_accelerometer_bucket_name(walking_information_dto.id), accelerometer_file),
            (
                get_atmospheric_pressure_bucket_name(walking_information_dto.id),
                atmospheric_pressure_file,
            ),
        ]
        file_service.upload_all(key_file)

        # パーティクルフィルタによるトラッキングを実行
        # tracking_particle = TrackingParticle()  # noqa: ERA001

        return GenerateTrajectoryServiceDto(
            trajectory_id=trajectory_id,
            walking_information_id=walking_information_dto.id,
            floor_information_id=floor_information_id,
            pedestrian_id=pedestrian_id,
            is_walking=True,
        )
