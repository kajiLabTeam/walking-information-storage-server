from app.application.dto import GenerateTrajectoryServiceDto
from app.infrastructure.connection import DBConnection, MinIOConnection
from app.infrastructure.external.services import FileService
from app.infrastructure.persistence.models import WalkingInformation
from app.infrastructure.persistence.models.trajectory import Trajectory
from app.infrastructure.persistence.repository import (
    TrajectoryRepository,
    WalkingInformationRepository,
)
from app.utils import (
    generate_ulid,
    get_accelerometer_bucket_name,
    get_atmospheric_pressure_bucket_name,
    get_gps_bucket_name,
    get_gyroscope_bucket_name,
    get_ratio_wave_bucket_name,
)


class GenerateTrajectoryService:
    def __init__(
        self,
    ) -> None:
        pass

    def run(
        self,
        pedestrian_id: str,
        floor_information_id: str,
        gps_file: bytes,
        wifi_file: bytes,
        gyroscope_file: bytes,
        accelerometer_file: bytes,
        atmospheric_pressure_file: bytes,
    ) -> GenerateTrajectoryServiceDto:
        s3 = MinIOConnection.connect()
        session = DBConnection.get_session()

        file_service = FileService(s3)
        trajectory_repo = TrajectoryRepository(session)
        # estimated_position_repo = EstimatedPositionRepository(session)  # noqa: ERA001
        walking_information_repo = WalkingInformationRepository(session)

        trajectory_record = trajectory_repo.save(
            Trajectory(
                id=str(generate_ulid()),
                is_walking=False,
                pedestrian_id=pedestrian_id,
                floor_id=floor_information_id,
            )
        )

        # walking_informationテーブルにデータを保存
        walking_information_record = walking_information_repo.save(
            WalkingInformation(
                id=str(generate_ulid()),
                pedestrian_id=pedestrian_id,
            )
        )

        # センサデータMinIOに保存
        key_file: list[tuple[str, bytes]] = [
            (get_gps_bucket_name(walking_information_record.id), gps_file),
            (get_ratio_wave_bucket_name(walking_information_record.id), wifi_file),
            (get_gyroscope_bucket_name(walking_information_record.id), gyroscope_file),
            (get_accelerometer_bucket_name(walking_information_record.id), accelerometer_file),
            (
                get_atmospheric_pressure_bucket_name(walking_information_record.id),
                atmospheric_pressure_file,
            ),
        ]
        file_service.upload_all(key_file)

        # パーティクルフィルタによるトラッキングを実行
        # tracking_particle = TrackingParticle()  # noqa: ERA001

        s3.close()
        session.close()

        return GenerateTrajectoryServiceDto(
            trajectory_id=trajectory_record.id,
            walking_information_id=walking_information_record.id,
            floor_information_id=floor_information_id,
            pedestrian_id=pedestrian_id,
            is_walking=True,
        )
