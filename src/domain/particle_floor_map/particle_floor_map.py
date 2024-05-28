from PIL.Image import Image

from config.const.color import (CANDIDATE_PARTICLES_COLOR,
                                PARTICLE_OUTLINE_COLOR)
from domain.estimated_particle.estimated_particle import EstimatedParticle
from domain.floor_map.floor_map import FloorMap


class ParticleFloorMap:
    @staticmethod
    def generate_image(
        floor_map: FloorMap,
        estimated_particle: EstimatedParticle,
    ) -> Image:
        """
        ## 推定されたパーティクルの軌跡をGIFアニメーションとして生成する
        """
        # images_cluster: List[Image] = []
        floor_map_copy = floor_map.clone()

        # パーティクルの位置を描画
        for particle in estimated_particle:
            floor_map_copy.depict_circle(
                position=(particle.get_x(), particle.get_y()),
                color=CANDIDATE_PARTICLES_COLOR,
                outline_color=PARTICLE_OUTLINE_COLOR,
            )

        floor_map_copy.get_floor_map().copy().save(
            "particle_floor_map.png",
        )

        # images_cluster.append(floor_map_copy.get_floor_map().copy())

        return floor_map_copy.get_floor_map().copy()
