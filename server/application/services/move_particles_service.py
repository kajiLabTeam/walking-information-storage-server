from PIL import Image

from config.const.path import IMAGE_PATH
from domain.models.floor_map.floor_map import FloorMap
from domain.models.particle_floor_map.particle_floor_map import \
    ParticleFloorMap
from domain.models.tracking_particle.tracking_particle import TrackingParticle
from domain.models.walking_parameter.walking_parameter import WalkingParameter
from domain.repository_impl.walking_sample_repository_impl import \
    WalkingSampleRepositoryImpl


class MoveParticlesService:
    def __init__(
        self,
        # walking_sample_repository: WalkingSampleRepositoryImpl,
    ):
        pass
        # self.__walking_sample_repository = walking_sample_repository

    def run(self, walking_parameter: WalkingParameter) -> WalkingParameter:
        floor_image_path = f"{IMAGE_PATH}/floor1.png"
        floor_image = Image.open(floor_image_path)
        floor_map = FloorMap(floor_image)
        tracking_particle = TrackingParticle(floor_map=floor_map)
        tracking_particle.track(walking_parameter)

        print(walking_parameter.get_angle_variation())
        print(walking_parameter.get_stride())

        ParticleFloorMap.generate_image(
            floor_map=floor_map,
            estimated_particle=tracking_particle.last_estimation_particles(),
        )

        return walking_parameter
