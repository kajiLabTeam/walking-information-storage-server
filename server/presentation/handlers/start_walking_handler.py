from application.services.start_walking_service import StartWalkingService
from fastapi import APIRouter, HTTPException
from infrastructure.persistence.repository.trajectory_repository import (
    RealtimeTrajectoryRepository,
    TrajectoryRepository,
)
from pydantic import BaseModel


class StartWalkingRequest(BaseModel):
    pedestrian_id: str
    floor_map_id: str


class StartWalkingResponse(BaseModel):
    trajectory_id: str


router = APIRouter()

start_walking_service = StartWalkingService(
    trajectory_repo=TrajectoryRepository(),
    realtime_trajectory_repo=RealtimeTrajectoryRepository(),
)


@router.post("/api/walk/start", response_model=StartWalkingResponse, status_code=201)
async def start_walking(request: StartWalkingRequest):
    """
    クライアントが歩行を開始することをサーバに通知するためのエンドポイント
    """
    try:
        trajectory_id = start_walking_service.run(
            pedestrian_id=request.pedestrian_id,
            floor_map_id=request.floor_map_id,
        )

        return StartWalkingResponse(trajectory_id=trajectory_id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
