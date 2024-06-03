import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter()

image_path = "particle_floor_map.png"


@router.get("/api/floor_map/get", status_code=200)
async def get_particles_floor_map():
    try:
        if not os.path.exists(image_path):
            return {"error": "File not found"}

        return FileResponse(image_path, media_type="image/png")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
