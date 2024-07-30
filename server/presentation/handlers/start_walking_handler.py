from application.services.start_walking_service import StartWalkingService
from fastapi import APIRouter, HTTPException
from infrastructure.persistence.repository.trajectory_repository import (
    RealtimeTrajectoryRepository,
    TrajectoryRepository,
)
from pydantic import BaseModel


class StartWalkingRequest(BaseModel):
    pedestrianId: str
    floorMapId: str


class StartWalkingResponse(BaseModel):
    trajectoryId: str


router = APIRouter()

start_walking_service = StartWalkingService(
    trajectory_repo=TrajectoryRepository(),
    realtime_trajectory_repo=RealtimeTrajectoryRepository(),
)


@router.post("/api/walking/start", response_model=StartWalkingResponse, status_code=201)
async def start_walking(request: StartWalkingRequest):
    """
    クライアントが歩行を開始することをサーバに通知するためのエンドポイント
    """
    try:
        trajectory_id = start_walking_service.run(
            pedestrian_id=request.pedestrianId,
            floor_map_id=request.floorMapId,
        )

        return StartWalkingResponse(trajectoryId=trajectory_id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
