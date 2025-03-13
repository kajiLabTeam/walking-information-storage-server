from typing import Annotated

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from pydantic import BaseModel

from app.application.services import GenerateTrajectoryService

router = APIRouter()

generate_trajectory_service = GenerateTrajectoryService()


class GenerateTrajectoryResponse(BaseModel):
    pedestrianId: str  # noqa: N815
    trajectoryId: str  # noqa: N815
    floorId: str  # noqa: N815
    floorInformationId: str  # noqa: N815


@router.post(
    "/api/trajectories",
    status_code=201,
)
async def generate_trajectory_handler(
    floorId: Annotated[str, Form()],  # noqa: N803
    pedestrianId: Annotated[str, Form()],  # noqa: N803
    gpsFile: Annotated[UploadFile, File()],  # noqa: N803
    wifiFile: Annotated[UploadFile, File()],  # noqa: N803
    gyroscopeFile: Annotated[UploadFile, File()],  # noqa: N803
    accelerometerFile: Annotated[UploadFile, File()],  # noqa: N803
    atmosphericPressureFile: Annotated[UploadFile, File()],  # noqa: N803
) -> GenerateTrajectoryResponse:
    """MinIOサーバへのファイルアップロード及びダウンロードが正常に行えるかを確認するためのエンドポイント."""
    try:
        result = generate_trajectory_service.run(
            pedestrian_id=pedestrianId,
            floor_id=floorId,
            gps_file=await gpsFile.read(),
            wifi_file=await wifiFile.read(),
            gyroscope_file=await gyroscopeFile.read(),
            accelerometer_file=await accelerometerFile.read(),
            atmospheric_pressure_file=await atmosphericPressureFile.read(),
        )

        return GenerateTrajectoryResponse(
            pedestrianId=result.pedestrian_id,
            trajectoryId=result.trajectory_id,
            floorId=floorId,
            floorInformationId=result.floor_information_id,
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        ) from e
