from PIL import Image

from config.const.path import IMAGE_PATH
from domain.floor_map.floor_map import FloorMap
from domain.tracking_particle.tracking_particle import TrackingParticle

floor_image_path = f"{IMAGE_PATH}/floor1.png"
floor_image = Image.open(floor_image_path)
floor_map = FloorMap(floor_image)
tracking_particle = TrackingParticle(floor_map=floor_map)


class GetParticlesFloorMapService:
    def __init__(
        self,
    ):
        pass
