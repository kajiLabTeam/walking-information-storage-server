from fastapi import APIRouter
from PIL import Image
from pydantic import BaseModel

from config.const.path import IMAGE_PATH
from domain.floor_map.floor_map import FloorMap
from domain.tracking_particle.tracking_particle import TrackingParticle


class MoveParticlesRequest(BaseModel):
    stride: int
    angleVariation: int


class MoveParticlesResponse(BaseModel):
    stride: int
    angleVariation: int


router = APIRouter()

image_path = "particle_floor_map.png"


@router.post("/api/particle/reset", status_code=201)
async def reset_particle():
    floor_image_path = f"{IMAGE_PATH}/floor1.png"
    floor_image = Image.open(floor_image_path)
    floor_map = FloorMap(floor_image)
    tracking_particle = TrackingParticle(floor_map=floor_map)
    tracking_particle.reset_instance()
