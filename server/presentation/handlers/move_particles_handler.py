from typing import Annotated

from application.services.move_particles_service import MoveParticlesService
from domain.models.angle_converter.angle_converter import AngleConverter
from domain.models.walking_parameter.walking_parameter import WalkingParameter
from fastapi import APIRouter, File, HTTPException, UploadFile
from pydantic import BaseModel


class MoveParticlesRequest(BaseModel):
    step: int
    angleVariation: int


class MoveParticlesResponse(BaseModel):
    step: int
    angleVariation: int


router = APIRouter()


@router.post("/api/walk", response_model=MoveParticlesResponse, status_code=201)
async def move_particles(
    rawDataFile: Annotated[UploadFile, File()],
):
    try:
        raw_data_file = await rawDataFile.read()
        angle_converter = AngleConverter(raw_data_file=raw_data_file)

        angle_variation = angle_converter.generate_correct_trajectory()

        move_particles_service = MoveParticlesService()
        walking_parameter = WalkingParameter(
            step=60,
            angle_variation=angle_variation,
        )
        move_particles_service.run(walking_parameter=walking_parameter)
        return MoveParticlesResponse(
            step=walking_parameter.get_step(),
            angleVariation=walking_parameter.get_angle_variation(),
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
