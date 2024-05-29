from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from application.services.move_particles_service import MoveParticlesService
from domain.walking_parameter.walking_parameter import WalkingParameter


class MoveParticlesRequest(BaseModel):
    stride: int
    angleVariation: int


class MoveParticlesResponse(BaseModel):
    stride: int
    angleVariation: int


router = APIRouter()


@router.post("/api/walk", response_model=MoveParticlesResponse, status_code=201)
async def move_particles(move_particles_request: MoveParticlesRequest):
    try:
        move_particles_service = MoveParticlesService()
        walking_parameter = WalkingParameter(
            stride=move_particles_request.stride,
            angle_variation=move_particles_request.angleVariation,
        )
        move_particles_service.run(walking_parameter=walking_parameter)
        return MoveParticlesResponse(
            stride=move_particles_request.stride,
            angleVariation=move_particles_request.angleVariation,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
