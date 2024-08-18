from typing import Annotated

from application.services.move_pedestrian_service import CreateWalkingSampleService
from fastapi import APIRouter, File, Form, UploadFile
from infrastructure.persistence.repository.floor_repository import FloorMapRepository
from infrastructure.persistence.repository.trajectory_repository import (
    TrajectoryRepository,
)
from infrastructure.persistence.repository.walking_information_repository import (
    GyroscopeRepository,
    WalkingInformationRepository,
)
from infrastructure.persistence.repository.walking_sample_repository import (
    EstimatedPositionRepository,
    ParticleRepository,
    WalkingSampleRepository,
)
from pydantic import BaseModel


class CreateWalkingSampleResponse(BaseModel):
    x: int
    y: int
    direction: int
    step: int
    angleChanged: int


router = APIRouter()

move_pedestrian_service = CreateWalkingSampleService(
    particle_repo=ParticleRepository(),
    floor_map_repo=FloorMapRepository(),
    gyroscope_repo=GyroscopeRepository(),
    trajectory_repo=TrajectoryRepository(),
    walking_sample_repo=WalkingSampleRepository(),
    estimated_position_repo=EstimatedPositionRepository(),
    walking_information_repo=WalkingInformationRepository(),
)


@router.post("/api/walk", response_model=CreateWalkingSampleResponse, status_code=201)
async def move_pedestrian(
    floorId: Annotated[str, Form()],
    pedestrianId: Annotated[str, Form()],
    trajectoryId: Annotated[str, Form()],
    gyroscopeFile: Annotated[UploadFile, File()],
):
    """
    クライアントが歩行開始からの歩行データをサーバに送信するためのエンドポイント
    """
    raw_data_file = await gyroscopeFile.read()

    estimated_position, walking_parameter = move_pedestrian_service.run(
        floor_id=floorId,
        pedestrian_id=pedestrianId,
        trajectory_id=trajectoryId,
        raw_data_file=raw_data_file,
    )

    return CreateWalkingSampleResponse(
        x=estimated_position.get_x(),
        y=estimated_position.get_y(),
        direction=int(estimated_position.get_direction()),
        step=walking_parameter.get_step(),
        angleChanged=walking_parameter.get_angle_changed(),
    )
