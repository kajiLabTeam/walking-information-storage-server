from typing import Tuple

from config.const.amount import STEP
from config.const.bucket import FLOOR_MAP_IMAGE_BUCKET_NAME, GYROSCOPE_FILE_BUCKET_NAME
from config.const.extension import FLOOR_MAP_EXTENSION, GYROSCOPE_EXTENSION
from domain.models.angle_converter.angle_converter import AngleConverter
from domain.models.estimated_particle.estimated_particle import (
    EstimatedParticle,
    EstimatedParticleFactory,
)
from domain.models.estimated_position.estimated_position import EstimatedPosition
from domain.models.floor_map.floor_map import FloorMap
from domain.models.walking_parameter.walking_parameter import WalkingParameter
from domain.repository_impl.trajectory_repository_impl import TrajectoryRepositoryImpl
from domain.repository_impl.walking_information_repository_impl import (
    GyroscopeRepositoryImpl,
    WalkingInformationRepositoryImpl,
)
from domain.repository_impl.walking_sample_repository_impl import (
    EstimatedPositionRepositoryImpl,
    ParticleRepositoryImpl,
    WalkingSampleRepositoryImpl,
)
from infrastructure.connection import DBConnection, MinIOConnection
from infrastructure.external.services.file_service import FileService

from server.domain.repository_impl.floor_repository_impl import (
    FloorMapImageRepositoryImpl,
)


class CreateWalkingSampleService:
    def __init__(
        self,
        particle_repo: ParticleRepositoryImpl,
        gyroscope_repo: GyroscopeRepositoryImpl,
        trajectory_repo: TrajectoryRepositoryImpl,
        walking_sample_repo: WalkingSampleRepositoryImpl,
        floor_map_image_repo: FloorMapImageRepositoryImpl,
        estimated_position_repo: EstimatedPositionRepositoryImpl,
        walking_information_repo: WalkingInformationRepositoryImpl,
    ):
        self.__particle_repo = particle_repo
        self.__gyroscope_repo = gyroscope_repo
        self.__trajectory_repo = trajectory_repo
        self.__walking_sample_repo = walking_sample_repo
        self.__floor_map_image_repo = floor_map_image_repo
        self.__estimated_position_repo = estimated_position_repo
        self.__walking_information_repo = walking_information_repo

    def run(
        self,
        pedestrian_id: str,
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
        walking_sample_id = self.__walking_sample_repo.find_latest_id_for_trajectory_id(
            conn=conn, trajectory_id=trajectory_id
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
        if walking_sample_id is None:
            estimated_particle = EstimatedParticleFactory.create(
                floor_map=floor_map,
                initial_walking_parameter=walking_parameter,
            )
        else:
            # 最新のパーティクルの状態を取得
            latest_particle_collection = (
                self.__particle_repo.find_for_walking_sample_id(
                    conn=conn, walking_sample_id=walking_sample_id
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
        walking_sample = self.__walking_sample_repo.save(
            conn=conn,
            is_converged=move_estimation_particles.is_converged(),
            trajectory_id=trajectory_id,
        )
        _ = self.__particle_repo.save_all(
            conn=conn,
            walking_sample_id=walking_sample.get_id(),
            particle_collection=move_estimation_particles.get_particle_collection(),
        )

        # 推定位置を保存
        self.__estimated_position_repo.save(
            conn=conn,
            estimated_position=estimated_position,
            walking_sample_id=walking_sample.get_id(),
        )

        # 歩行情報を保存
        walking_information_id = self.__walking_information_repo.save(
            conn=conn,
            pedestrian_id=pedestrian_id,
        )

        gyroscope_id = self.__gyroscope_repo.save(
            conn=conn,
            walking_information_id=walking_information_id,
        )
        file_service.upload(
            bucket_type_name=GYROSCOPE_FILE_BUCKET_NAME,
            bucket_id=f"{trajectory_id}/{gyroscope_id}.{GYROSCOPE_EXTENSION}",
            file=raw_data_file,
        )

        return estimated_position, walking_parameter
