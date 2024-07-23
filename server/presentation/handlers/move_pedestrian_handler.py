from typing import Annotated

from fastapi import APIRouter, File, HTTPException, UploadFile
from pydantic import BaseModel

from application.services.move_pedestrian_service import CreateWalkingSampleService
from config.const.amount import STEP
from domain.models.angle_converter.angle_converter import AngleConverter
from domain.models.walking_parameter.walking_parameter import WalkingParameter
from infrastructure.persistence.repository.coordinate_repository import (
    RealtimeCoordinateRepository,
)
from infrastructure.persistence.repository.floor_map_repository import (
    FloorMapImageRepository,
)
from infrastructure.persistence.repository.particle_repository import ParticleRepository
from infrastructure.persistence.repository.raw_data_repository import RawDataRepository
from infrastructure.persistence.repository.trajectory_repository import (
    RealtimeTrajectoryRepository,
)
from infrastructure.persistence.repository.walking_sample_repository import (
    RealtimeWalkingSampleRepository,
)


class CreateWalkingSampleRequest(BaseModel):
    step: int
    angleVariation: int


class CreateWalkingSampleResponse(BaseModel):
    x: int
    y: int
    direction: int
    step: int
    angleChanged: int


router = APIRouter()

move_pedestrian_service = CreateWalkingSampleService(
    raw_data_repo=RawDataRepository(),
    particle_repo=ParticleRepository(),
    floor_map_image_repo=FloorMapImageRepository(),
    realtime_coordinate_repo=RealtimeCoordinateRepository(),
    realtime_trajectory_repo=RealtimeTrajectoryRepository(),
    realtime_walking_sample_repo=RealtimeWalkingSampleRepository(),
)


@router.post("/api/walk", response_model=CreateWalkingSampleResponse, status_code=201)
async def move_particles(
    trajectoryId: str,
    rawDataFile: Annotated[UploadFile, File()],
):
    try:
        raw_data_file = await rawDataFile.read()

        angle_converter = AngleConverter(raw_data_file=raw_data_file)
        angle_changed = angle_converter.calculate_cumulative_angle()

        walking_parameter = WalkingParameter(
            id=None,
            step=STEP,
            angle_changed=angle_changed,
        )

        estimated_position = move_pedestrian_service.run(
            trajectory_id=trajectoryId,
            raw_data_file=raw_data_file,
            walking_parameter=walking_parameter,
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
