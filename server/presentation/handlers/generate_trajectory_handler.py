from typing import Annotated

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from server.application.services import GenerateTrajectoryService
from server.infrastructure.persistence.repository import (
    CorrectPositionRepository,
    EstimatedPositionRepository,
    FloorInformationRepository,
    TrajectoryRepository,
    WalkingInformationRepository,
)

generate_trajectory_service = GenerateTrajectoryService(
    correct_position_repo=CorrectPositionRepository(),
    estimated_position_repo=EstimatedPositionRepository(),
    floor_information_repo=FloorInformationRepository(),
    trajectory_repo=TrajectoryRepository(),
    walking_information_repo=WalkingInformationRepository(),
)
router = APIRouter()


@router.post(
    "/api/trajectories",
    status_code=201,
)
async def generate_trajectory_handler(
    pedestrianId: Annotated[str, Form()],  # noqa: N803
    trajectoryId: Annotated[str, Form()],  # noqa: N803
    gpsFile: Annotated[UploadFile, File()],  # noqa: N803
    wifiFile: Annotated[UploadFile, File()],  # noqa: N803
    gyroscopeFile: Annotated[UploadFile, File()],  # noqa: N803
    accelerometerFile: Annotated[UploadFile, File()],  # noqa: N803
    atmosphericPressureFile: Annotated[UploadFile, File()],  # noqa: N803
) -> None:
    """MinIOサーバへのファイルアップロード及びダウンロードが正常に行えるかを確認するためのエンドポイント."""
    try:
        generate_trajectory_service.run(
            pedestrian_id=pedestrianId,
            trajectory_id=trajectoryId,
            floor_information_id="",
            gps_file=await gpsFile.read(),
            wifi_file=await wifiFile.read(),
            gyroscope_file=await gyroscopeFile.read(),
            accelerometer_file=await accelerometerFile.read(),
            atmospheric_pressure_file=await atmosphericPressureFile.read(),
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        ) from e
