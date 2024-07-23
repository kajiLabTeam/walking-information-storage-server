from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from application.services.finish_walking_service import FinishWalkingService
from infrastructure.persistence.repository.trajectory_repository import (
    TrajectoryRepository,
)


class FinishWalkingRequest(BaseModel):
    trajectory_id: str


class FinishWalkingResponse(BaseModel):
    trajectory_id: str


router = APIRouter()

finish_walking_service = FinishWalkingService(trajectory_repo=TrajectoryRepository())


@router.post("/api/walk", response_model=FinishWalkingRequest, status_code=201)
async def move_particles(finish_walking_request: FinishWalkingRequest):
    try:
        trajectory_id = finish_walking_request.trajectory_id

        finish_walking_service.run(trajectory_id=trajectory_id)

        return FinishWalkingResponse(trajectory_id=trajectory_id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
