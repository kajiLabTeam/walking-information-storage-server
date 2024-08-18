from typing import Annotated

from application.services.move_pedestrian_service import CreateWalkingSampleService
from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from infrastructure.persistence.repository.coordinate_repository import (
    RealtimeCoordinateRepository,
)
from infrastructure.persistence.repository.floor_map_repository import (
    FloorMapImageRepository,
)
from infrastructure.persistence.repository.gyroscope_repository import (
    GyroscopeRepository,
)
from infrastructure.persistence.repository.particle_repository import ParticleRepository
from infrastructure.persistence.repository.trajectory_repository import (
    RealtimeTrajectoryRepository,
    TrajectoryRepository,
)
from infrastructure.persistence.repository.walking_sample_repository import (
    RealtimeWalkingSampleRepository,
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
    gyroscope_repo=GyroscopeRepository(),
    trajectory_repo=TrajectoryRepository(),
    floor_map_image_repo=FloorMapImageRepository(),
    realtime_coordinate_repo=RealtimeCoordinateRepository(),
    realtime_trajectory_repo=RealtimeTrajectoryRepository(),
    realtime_walking_sample_repo=RealtimeWalkingSampleRepository(),
)


@router.post("/api/walk", response_model=CreateWalkingSampleResponse, status_code=201)
async def move_pedestrian(
    pedestrianId: Annotated[str, Form()],
    trajectoryId: Annotated[str, Form()],
    gyroscopeFile: Annotated[UploadFile, File()],
):
    """
    クライアントが歩行開始からの歩行データをサーバに送信するためのエンドポイント
    """
    try:
        raw_data_file = await gyroscopeFile.read()

        estimated_position, walking_parameter = move_pedestrian_service.run(
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

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
