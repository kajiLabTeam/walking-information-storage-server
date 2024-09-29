from typing import Annotated

from application.services.move_pedestrian_service import MovePedestrianService
from fastapi import APIRouter, File, Form, UploadFile
from infrastructure.persistence.repository.floor_repository import (
    FloorInformationRepository,
    FloorMapRepository,
    FloorRepository,
)
from infrastructure.persistence.repository.trajectory_repository import (
    TrajectoryRepository,
)
from infrastructure.persistence.repository.walking_information_repository import (
    AccelerometerRepository,
    AtmosphericPressureRepository,
    GpsRepository,
    GyroscopeRepository,
    RatioWaveRepository,
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
    direction: float
    step: int
    angleChanged: int


router = APIRouter()

move_pedestrian_service = MovePedestrianService(
    floor_repo=FloorRepository(),
    particle_repo=ParticleRepository(),
    floor_map_repo=FloorMapRepository(),
    gps_repo=GpsRepository(),
    ratio_wave_repo=RatioWaveRepository(),
    gyroscope_repo=GyroscopeRepository(),
    accelerometer_repo=AccelerometerRepository(),
    atmospheric_pressure_repo=AtmosphericPressureRepository(),
    trajectory_repo=TrajectoryRepository(),
    walking_sample_repo=WalkingSampleRepository(),
    floor_information_repo=FloorInformationRepository(),
    estimated_position_repo=EstimatedPositionRepository(),
    walking_information_repo=WalkingInformationRepository(),
)


@router.post("/api/walk", response_model=CreateWalkingSampleResponse, status_code=201)
async def move_pedestrian(
    pedestrianId: Annotated[str, Form()],
    trajectoryId: Annotated[str, Form()],
    gpsFile: Annotated[UploadFile, File()],
    wifiFile: Annotated[UploadFile, File()],
    gyroscopeFile: Annotated[UploadFile, File()],
    accelerometerFile: Annotated[UploadFile, File()],
    atmosphericPressureFile: Annotated[UploadFile, File()],
):
    """
    クライアントが歩行開始からの歩行データをサーバに送信するためのエンドポイント
    """
    gps_file = await gpsFile.read()
    wifi_file = await wifiFile.read()
    gyroscope_file = await gyroscopeFile.read()
    accelerometer_file = await accelerometerFile.read()
    atmospheric_pressure_file = await atmosphericPressureFile.read()

    move_pedestrian_service_dto = move_pedestrian_service.run(
        pedestrian_id=pedestrianId,
        trajectory_id=trajectoryId,
        gps_file=gps_file,
        wifi_file=wifi_file,
        gyroscope_file=gyroscope_file,
        accelerometer_file=accelerometer_file,
        atmospheric_pressure_file=atmospheric_pressure_file,
    )

    return CreateWalkingSampleResponse(
        x=move_pedestrian_service_dto.estimated_position.get_x(),
        y=move_pedestrian_service_dto.estimated_position.get_y(),
        direction=move_pedestrian_service_dto.estimated_position.get_direction(),
        step=move_pedestrian_service_dto.walking_parameter.get_step(),
        angleChanged=move_pedestrian_service_dto.walking_parameter.get_angle_changed(),
    )
