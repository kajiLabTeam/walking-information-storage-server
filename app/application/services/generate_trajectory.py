from typing import TYPE_CHECKING

from app.application.dto import GenerateTrajectoryServiceDto
from app.application.errors.application_error import ApplicationError, ApplicationErrorType
from app.domain.models.floor_map.floor_map import FloorMap
from app.domain.models.tracking_particle.tracking_particle import TrackingParticle
from app.domain.models.walking_parameter_collection.walking_parameter_collection import (
    WalkingParameterCollection,
)
from app.infrastructure.connection import DBConnection, MinIOConnection
from app.infrastructure.external.services import FileService
from app.infrastructure.persistence.models import Trajectory, WalkingInformation
from app.infrastructure.persistence.models.trajectory import EstimatedPosition
from app.infrastructure.persistence.repository import (
    EstimatedPositionRepository,
    FloorInformationRepository,
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
from app.utils.bucket import get_floor_map_bucket_name

if TYPE_CHECKING:
    from app.domain.dataclasses.coordinate import Pose


class GenerateTrajectoryService:
    def __init__(
        self,
    ) -> None:
        pass

    def run(
        self,
        pedestrian_id: str,
        floor_id: str,
        gps_file: bytes,
        wifi_file: bytes,
        gyroscope_file: bytes,
        accelerometer_file: bytes,
        atmospheric_pressure_file: bytes,
    ) -> GenerateTrajectoryServiceDto:
        s3 = MinIOConnection.connect()
        session = DBConnection.get_session()

        file_service = FileService(s3)
        floor_information_repo = FloorInformationRepository(session)
        trajectory_repo = TrajectoryRepository(session)
        estimated_position_repo = EstimatedPositionRepository(session)
        walking_information_repo = WalkingInformationRepository(session)
        trajectory_record = trajectory_repo.save(
            Trajectory(
                id=str(generate_ulid()),
                is_walking=False,
                pedestrian_id=pedestrian_id,
                floor_id=floor_id,
            )
        )
        walking_information_record = walking_information_repo.save(
            WalkingInformation(
                id=str(generate_ulid()),
                pedestrian_id=pedestrian_id,
            )
        )
        floor_information_record = floor_information_repo.get_latest_by_floor_id(floor_id)
        if floor_information_record is None:
            raise ApplicationError(
                ApplicationErrorType.NOT_FLOOR_INFORMATION, 404, "Not found floor information"
            )

        session.flush()

        session.refresh(trajectory_record)
        session.refresh(floor_information_record)
        session.refresh(walking_information_record)

        trajectory_id = trajectory_record.id
        floor_information_id = floor_information_record.id
        walking_information_id = walking_information_record.id

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

        floor_map_image = file_service.download(
            get_floor_map_bucket_name(floor_id=floor_id, floor_information_id=floor_information_id)
        )
        floor_map = FloorMap(floor_map_image_bytes=floor_map_image)

        walking_parameter_collection = WalkingParameterCollection(
            gyroscope_file=gyroscope_file,
            accelerometer_file=accelerometer_file,
        )

        # パーティクルフィルタによるトラッキングを実行
        tracking_particle = TrackingParticle(
            floor_map=floor_map,
            walking_parameter_collection=walking_parameter_collection,
        )
        tracking_particle.track()

        estimated_pose_collection: list[Pose] = [
            estimation_particle.get_estimated_pose()
            for estimation_particle in tracking_particle.get_estimation_particles()
        ]

        # トラッキング結果を保存
        for estimated_pose in estimated_pose_collection:
            estimated_position_repo.save(
                EstimatedPosition(
                    id=str(generate_ulid()),
                    x=estimated_pose.coordinate.x,
                    y=estimated_pose.coordinate.y,
                    is_converged=False,
                    direction=int(estimated_pose.direction),
                    trajectory_id=trajectory_id,
                    walking_information_id=walking_information_id,
                )
            )

        session.commit()

        s3.close()
        session.close()

        return GenerateTrajectoryServiceDto(
            trajectory_id=trajectory_id,
            walking_information_id=walking_information_id,
            floor_information_id=floor_information_id,
            pedestrian_id=pedestrian_id,
            is_walking=True,
        )
