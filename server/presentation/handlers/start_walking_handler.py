from application.services.start_walking_service import StartWalkingService
from fastapi import APIRouter, HTTPException
from infrastructure.persistence.repository.floor_repository import (
    FloorInformationRepository,
)
from infrastructure.persistence.repository.trajectory_repository import (
    TrajectoryRepository,
)
from pydantic import BaseModel


class StartWalkingRequest(BaseModel):
    pedestrianId: str
    floorId: str


class StartWalkingResponse(BaseModel):
    trajectoryId: str
    floorInformationId: str


router = APIRouter()

start_walking_service = StartWalkingService(
    trajectory_repo=TrajectoryRepository(),
    floor_information_repo=FloorInformationRepository(),
)


@router.post("/api/walking/start", response_model=StartWalkingResponse, status_code=201)
async def start_walking(request: StartWalkingRequest):
    """
    クライアントが歩行を開始することをサーバに通知するためのエンドポイント
    """
    try:
        start_walking_service_dto = start_walking_service.run(
            pedestrian_id=request.pedestrianId,
            floor_id=request.floorId,
        )

        return StartWalkingResponse(
            trajectoryId=start_walking_service_dto.trajectory_id,
            floorInformationId=start_walking_service_dto.floor_information_id,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
