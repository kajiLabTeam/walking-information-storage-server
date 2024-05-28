from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from application.services.move_particles_service import MoveParticlesService


class MoveParticlesRequest(BaseModel):
    stride: int
    angleVariation: int


class MoveParticlesResponse(BaseModel):
    stride: int
    angleVariation: int


router = APIRouter()


@router.post("/api/particles/reset", status_code=201)
async def reset_particles():
    try:
        print("reset")
        move_particles_service = MoveParticlesService()

        move_particles_service.reset()

        return {"message": "ok"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e