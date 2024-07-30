from typing import Tuple

from config.const.amount import STEP
from config.const.bucket import FLOOR_MAP_IMAGE_BUCKET_NAME, RAW_DATA_FILE_BUCKET_NAME
from config.const.extension import FLOOR_MAP_EXTENSION, RAW_DATA_EXTENSION
from domain.models.angle_converter.angle_converter import AngleConverter
from domain.models.estimated_particle.estimated_particle import (
    EstimatedParticle,
    EstimatedParticleFactory,
)
from domain.models.estimated_position.estimated_position import EstimatedPosition
from domain.models.floor_map.floor_map import FloorMap
from domain.models.walking_parameter.walking_parameter import WalkingParameter
from domain.repository_impl.coordinate_repository_impl import (
    RealtimeCoordinateRepositoryImpl,
)
from domain.repository_impl.floor_map_repository_impl import FloorMapImageRepositoryImpl
from domain.repository_impl.particle_repository_impl import ParticleRepositoryImpl
from domain.repository_impl.raw_data_repository_impl import RawDataRepositoryImpl
from domain.repository_impl.trajectory_repository_impl import (
    RealtimeTrajectoryRepositoryImpl,
    TrajectoryRepositoryImpl,
)
from domain.repository_impl.walking_sample_repository_impl import (
    RealtimeWalkingSampleRepositoryImpl,
)
from infrastructure.connection import DBConnection, MinIOConnection
from infrastructure.external.services.file_service import FileService


class CreateWalkingSampleService:
    def __init__(
        self,
        raw_data_repo: RawDataRepositoryImpl,
        particle_repo: ParticleRepositoryImpl,
        trajectory_repo: TrajectoryRepositoryImpl,
        floor_map_image_repo: FloorMapImageRepositoryImpl,
        realtime_coordinate_repo: RealtimeCoordinateRepositoryImpl,
        realtime_trajectory_repo: RealtimeTrajectoryRepositoryImpl,
        realtime_walking_sample_repo: RealtimeWalkingSampleRepositoryImpl,
    ):
        self.__raw_data_repo = raw_data_repo
        self.__particle_repo = particle_repo
        self.__trajectory_repo = trajectory_repo
        self.__floor_map_image_repo = floor_map_image_repo
        self.__realtime_coordinate_repo = realtime_coordinate_repo
        self.__realtime_trajectory_repo = realtime_trajectory_repo
        self.__realtime_walking_sample_repo = realtime_walking_sample_repo

    def run(
        self,
        trajectory_id: str,
        raw_data_file: bytes,
    ) -> Tuple[EstimatedPosition, WalkingParameter]:
        conn = DBConnection.connect()
        s3 = MinIOConnection.connect()
        file_service = FileService(s3)

        # 歩行データから、歩行パラメータを取得
        angle_converter = AngleConverter(raw_data_file=raw_data_file)
        angle_changed = angle_converter.calculate_cumulative_angle()
        walking_parameter = WalkingParameter(
            id=None,
            step=STEP,
            angle_changed=angle_changed,
        )

        # 引数のidを元に、必要な情報を取得
        realtime_id = self.__realtime_trajectory_repo.find_for_trajectory_id(
            conn=conn, trajectory_id=trajectory_id
        )
        realtime_walking_sample_id = (
            self.__realtime_walking_sample_repo.find_latest_id_for_realtime_id(
                conn=conn, realtime_id=realtime_id
            )
        )

        floor_map_id = self.__trajectory_repo.find_for_id(
            conn=conn, trajectory_id=trajectory_id
        )
        floor_map_image_id = self.__floor_map_image_repo.find_for_floor_map_id(
            conn=conn, floor_map_id=floor_map_id
        )

        floor_map_image_bytes = file_service.download(
            bucket_type_name=FLOOR_MAP_IMAGE_BUCKET_NAME,
            bucket_id=f"{floor_map_id}/{floor_map_image_id}.{FLOOR_MAP_EXTENSION}",
        )
        floor_map = FloorMap(
            floor_map_image_bytes=floor_map_image_bytes,
        )

        # 歩行サンプルがない場合は、初期のパーティクルを生成
        if realtime_walking_sample_id is None:
            estimated_particle = EstimatedParticleFactory.create(
                floor_map=floor_map,
                initial_walking_parameter=walking_parameter,
            )
        else:
            # 最新のパーティクルの状態を取得
            latest_particle_collection = (
                self.__particle_repo.find_for_realtime_walking_sample_id(
                    conn=conn, realtime_walking_sample_id=realtime_walking_sample_id
                )
            )
            estimated_particle = EstimatedParticle(
                floor_map=floor_map,
                current_walking_parameter=walking_parameter,
                particle_collection=latest_particle_collection,
            )

        estimated_particle = EstimatedParticleFactory.create(
            floor_map=floor_map, initial_walking_parameter=walking_parameter
        )

        # パーティクルフィルタの実行
        estimated_particle.remove_by_floor_map()
        move_estimation_particles = estimated_particle.move(
            current_walking_parameter=walking_parameter
        )
        move_estimation_particles.remove_by_floor_map()
        move_estimation_particles.remove_by_direction(step=walking_parameter.get_step())
        move_estimation_particles.resampling(step=walking_parameter.get_step())

        # その時点で、パーティクルフィルタをかけた時の推定位置を取得
        estimated_position = move_estimation_particles.estimate_position()

        # パーティクルフィルタの結果を保存
        realtime_walking_sample_insert_result = (
            self.__realtime_walking_sample_repo.save(
                conn=conn, realtime_id=realtime_id, walking_sample=walking_parameter
            )
        )
        _ = self.__particle_repo.save_all(
            conn=conn,
            realtime_walking_sample_id=realtime_walking_sample_insert_result.get_id(),
            particle_collection=move_estimation_particles.get_particle_collection(),
        )

        # 推定位置を保存
        _ = self.__realtime_coordinate_repo.save(
            conn=conn,
            realtime_walking_sample_id=realtime_walking_sample_insert_result.get_id(),
            estimated_position=estimated_position,
        )

        # 生データを保存
        raw_data_id = self.__raw_data_repo.save(
            conn=conn,
            realtime_walking_sample_id=realtime_walking_sample_insert_result.get_id(),
        )
        file_service.upload(
            bucket_type_name=RAW_DATA_FILE_BUCKET_NAME,
            bucket_id=f"{trajectory_id}/{raw_data_id}.{RAW_DATA_EXTENSION}",
            file=raw_data_file,
        )

        return estimated_position, walking_parameter
