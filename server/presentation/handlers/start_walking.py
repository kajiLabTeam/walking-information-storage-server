from fastapi import APIRouter, HTTPException
from PIL import Image
from pydantic import BaseModel

from config.const.path import IMAGE_PATH
from domain.models.floor_map.floor_map import FloorMap
from domain.models.tracking_particle.tracking_particle import TrackingParticle
from infrastructure.repository.trajectory import TrajectoryRepository


class StartWalkingResponse(BaseModel):
    trajectory_id: str


router = APIRouter()


@router.post("/api/walk/start", status_code=201)
async def start_walking():
    try:
        trajectory_repository = TrajectoryRepository()
        trajectory_id = trajectory_repository.save()

        return StartWalkingResponse(trajectory_id=trajectory_id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
