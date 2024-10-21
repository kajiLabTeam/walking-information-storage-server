from typing import List, Literal

import numpy as np
from config.const import (
    CLUSTER_AMOUNT_THRESHOLD,
    CONVERGENCE_DECENTRALIZATION_THRESHOLD,
    INITIAL_PARTICLES_AMOUNT,
    MISSING_PARTICLE_THRESHOLD,
    PARTICLES_ANGLE_ERROR,
    PARTICLES_DIRECTION_ERROR,
    PARTICLES_STEP_ERROR,
    REVERSE_RADIUS,
    SEARCH_NEAREST_INSIDE_RANGE,
)
from domain.models.estimated_particle.convergence_judgment import ConvergenceJudgment
from domain.models.estimated_position.estimated_position import EstimatedPosition
from domain.models.floor_map.floor_map import FloorMap
from domain.models.particle.particle import Particle
from domain.models.particle_collection.particle_collection import ParticleCollection
from domain.models.walking_parameter.walking_parameter import WalkingParameter
from utils import get_random_angle


class EstimatedParticle:
    def __init__(
        self,
        floor_map: FloorMap,
        current_walking_parameter: WalkingParameter,
        particle_collection: ParticleCollection,
    ):
        particle_collection.shuffle()

        self.__floor_map = floor_map
        self.__missing_particle_count = 0
        self.__current_walking_parameter = current_walking_parameter
        self.__particle_collection = particle_collection

    @classmethod
    def initialize(
        cls, floor_map: FloorMap, initial_walking_parameter: WalkingParameter
    ):
        """
        ## 初期パーティクルを散布する
        """
        particle_collection = ParticleCollection()

        while len(particle_collection) < INITIAL_PARTICLES_AMOUNT:
            x = np.random.randint(floor_map.get_map_width())
            y = np.random.randint(floor_map.get_map_height())
            direction = get_random_angle()
            weight = 1 / INITIAL_PARTICLES_AMOUNT

            if not floor_map.is_inside_floor(x=x, y=y):
                continue

            particle_collection.add(
                particle=Particle(
                    x=x,
                    y=y,
                    direction=direction,
                    weight=weight,
                )
            )

        return EstimatedParticle(
            floor_map=floor_map,
            current_walking_parameter=initial_walking_parameter,
            particle_collection=particle_collection,
        )

    @classmethod
    def reverse_initialize(
        cls,
        floor_map: FloorMap,
        final_position: EstimatedPosition,
        walking_parameter: WalkingParameter,
    ):
        """
        ## 逆算軌跡推定の際に行うパーティクルフィルタのパーティクルを散布する
        """

        particle_collection = ParticleCollection()

        while len(particle_collection) < INITIAL_PARTICLES_AMOUNT:
            x = final_position.get_x() + np.random.randint(
                -REVERSE_RADIUS, REVERSE_RADIUS
            )
            y = final_position.get_y() + np.random.randint(
                -REVERSE_RADIUS, REVERSE_RADIUS
            )
            direction = final_position.get_direction() + PARTICLES_DIRECTION_ERROR()
            weight = 1 / INITIAL_PARTICLES_AMOUNT

            if not floor_map.is_inside_floor(x=x, y=y):
                continue

            particle_collection.add(
                particle=Particle(
                    x=x,
                    y=y,
                    direction=direction,
                    weight=weight,
                )
            )

        return EstimatedParticle(
            floor_map=floor_map,
            current_walking_parameter=walking_parameter,
            particle_collection=particle_collection,
        )

    def get_floor_map(self) -> FloorMap:
        return self.__floor_map

    def get_missing_particle_count(self) -> int:
        return self.__missing_particle_count

    def get_current_walking_parameter(self) -> WalkingParameter:
        return self.__current_walking_parameter

    def get_particle_collection(self) -> ParticleCollection:
        return self.__particle_collection

    def is_converged(self) -> bool:
        """
        ## パーティクルのクラスタ数を計算する
        """
        X = np.array(
            [
                [particle.get_x(), particle.get_y()]
                for particle in self.__particle_collection
            ]
        )
        cluster_amount = ConvergenceJudgment.calculate_cluster_amount(X=X)

        if (
            cluster_amount <= CLUSTER_AMOUNT_THRESHOLD
            and self.get_convergence_ratio() >= CONVERGENCE_DECENTRALIZATION_THRESHOLD
        ):
            return True

        return False

    def get_particles_within_radius(
        self, x: int, y: int, radius: int
    ) -> "EstimatedParticle":
        """
        指定された座標を中心とする半径radiusの範囲内に存在するパーティクルを取得する
        """
        radius_squared = radius**2

        particles_within_radius = ParticleCollection()
        particles_within_radius.add_all(
            [
                particle
                for particle in self.__particle_collection
                if (particle.get_x() - x) ** 2 + (particle.get_y() - y) ** 2
                <= radius_squared
            ]
        )

        return EstimatedParticle(
            floor_map=self.__floor_map,
            current_walking_parameter=self.__current_walking_parameter,
            particle_collection=particles_within_radius,
        )

    def get_convergence_ratio(self) -> float:
        """
        ## パーティクルの分散をもとに、収束度を計算する
        """
        return 1 / self.__particle_collection.get_decentralization()

    def move(self, current_walking_parameter: WalkingParameter) -> "EstimatedParticle":
        """
        ## ベクトルの向きに合わせてパーティクルを移動させる
        """
        step = current_walking_parameter.get_step()
        changed_angle = current_walking_parameter.get_angle_changed()

        move_particle_collection = ParticleCollection()

        moved_particles = [
            particle.move(
                step=step,
                changed_angle=changed_angle,
                step_error=PARTICLES_STEP_ERROR(),
            )
            for particle in self.__particle_collection
        ]

        move_particle_collection.add_all(moved_particles)

        return EstimatedParticle(
            floor_map=self.__floor_map,
            current_walking_parameter=current_walking_parameter,
            particle_collection=move_particle_collection,
        )

    def estimate_position(self) -> EstimatedPosition:
        """
        ## 重みづけ平均を元に歩行座標を推定する
        """
        estimated_x = self.__particle_collection.get_x_mean()
        estimated_y = self.__particle_collection.get_y_mean()
        estimated_direction = self.__particle_collection.get_direction_mean()

        if not self.__floor_map.is_inside_floor(x=estimated_x, y=estimated_y):
            estimated_x, estimated_y = self.__floor_map.get_nearest_inside_coordinate(
                outside_position=(estimated_x, estimated_y),
                search_range=SEARCH_NEAREST_INSIDE_RANGE,
            )
        return EstimatedPosition(
            x=estimated_x,
            y=estimated_y,
            direction=estimated_direction,
        )

    def remove_by_floor_map(self):
        """
        ## パーティクルが歩行可能領域外に存在する場合、パーティクルを削除する
        """
        remove_particle_indexes = [
            i
            for i, particle in enumerate(self.__particle_collection)
            if not self.__floor_map.is_inside_floor(
                x=particle.get_x(), y=particle.get_y()
            )
        ]

        self.__missing_particle_count += len(remove_particle_indexes)

        self.__particle_collection.pop_all(indexes=remove_particle_indexes)

    def remove_by_direction(self, step: int):
        """
        ## パーティクルの向きが歩行不可能領域を向いている場合、パーティクルを削除する
        """
        remove_particle_indexes = []

        for i, particle in enumerate(self.__particle_collection):
            if particle.is_straight_direction_to_wall(
                step=step, is_inside_floor=self.__floor_map.is_inside_floor
            ):
                remove_particle_indexes.append(i)
                continue

            if particle.is_turn_direction_to_wall(
                step=step,
                is_inside_floor=self.__floor_map.is_inside_floor,
            ):
                remove_particle_indexes.append(i)

        self.__missing_particle_count += len(remove_particle_indexes)
        self.__particle_collection.pop_all(indexes=remove_particle_indexes)

    def resampling(self, step: int, mode: Literal["normal", "reversed"] = "normal"):
        """
        ## リサンプリングを実行する
        """
        placeable_count = self.__count_placeable()
        new_particles: List[Particle] = []

        if placeable_count >= MISSING_PARTICLE_THRESHOLD and mode == "normal":
            while placeable_count > 0:
                new_particle = Particle.create_random_particle(
                    x_range=self.__floor_map.get_map_width(),
                    y_range=self.__floor_map.get_map_height(),
                )
                new_particles.append(new_particle)
                placeable_count -= 1
                if placeable_count == 0:
                    break
        else:
            while placeable_count > 0:
                for particle in self.__particle_collection:
                    new_particle = particle.new(
                        weight=particle.get_weight(),
                        step=step,
                        direction_error=PARTICLES_ANGLE_ERROR(),
                    )
                    new_particles.append(new_particle)
                    placeable_count -= 1
                    if placeable_count == 0:
                        break

        self.__particle_collection.add_all(new_particles)

    def resampling_by_weight(self):
        num_particles = len(self.__particle_collection)
        weights = np.array([p.get_weight() for p in self.__particle_collection])

        # TODO 重みの正規化のロジックここじゃない
        weights /= np.sum(weights)

        # 累積分布関数（CDF）の計算
        cdf = np.cumsum(weights)

        # リサンプリング位置の決定
        positions = (np.arange(num_particles) + np.random.uniform(0, 1)) / num_particles

        new_particles: List[Particle] = []
        index = 0
        for pos in positions:
            while pos > cdf[index]:
                index += 1
            new_particle = self.__particle_collection[index].new(
                weight=1 / num_particles,
                step=1,
                direction_error=PARTICLES_ANGLE_ERROR(),
            )
            new_particles.append(new_particle)

        self.__particle_collection.reset()
        self.__particle_collection.add_all(new_particles)

    def __count_placeable(self) -> int:
        return INITIAL_PARTICLES_AMOUNT - len(self.__particle_collection)

    def __iter__(self):
        return iter(self.__particle_collection)

    def __len__(self):
        return len(self.__particle_collection)
