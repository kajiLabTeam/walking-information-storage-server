from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from server.application.services import StartWalkingService
from server.infrastructure.persistence.repository import (
    FloorInformationRepository,
    TrajectoryRepository,
)


class StartWalkingRequest(BaseModel):
    floorId: str  # noqa: N815
    pedestrianId: str  # noqa: N815


class StartWalkingResponse(BaseModel):
    trajectoryId: str  # noqa: N815
    floorInformationId: str  # noqa: N815


router = APIRouter()

start_walking_service = StartWalkingService(
    trajectory_repo=TrajectoryRepository(),
    floor_information_repo=FloorInformationRepository(),
)


@router.post(
    "/api/walking/start",
    status_code=201,
)
async def start_walking(
    request: StartWalkingRequest,
) -> StartWalkingResponse:
    """クライアントが歩行を開始することをサーバに通知するためのエンドポイント."""
    try:
        start_walking_service_dto = start_walking_service.run(
            pedestrian_id=request.pedestrianId,
        )

        return StartWalkingResponse(
            trajectoryId=start_walking_service_dto.trajectory_id,
            floorInformationId=start_walking_service_dto.floor_information_id,
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        ) from e
