from PIL import Image

from config.const.path import IMAGE_PATH
from domain.floor_map.floor_map import FloorMap
from domain.particle_floor_map.particle_floor_map import ParticleFloorMap
from domain.tracking_particle.tracking_particle import TrackingParticle
from domain.walking_parameter.walking_parameter import WalkingParameter

floor_image_path = f"{IMAGE_PATH}/floor1.png"
floor_image = Image.open(floor_image_path)
floor_map = FloorMap(floor_image)
tracking_particle = TrackingParticle(floor_map=floor_map)


class MoveParticlesService:
    def __init__(
        self,
    ):
        pass

    def run(self, walking_parameter: WalkingParameter) -> WalkingParameter:
        tracking_particle.track(walking_parameter)

        ParticleFloorMap.generate_image(
            floor_map=floor_map,
            estimated_particle=tracking_particle.last_estimation_particles(),
        )

        return walking_parameter
