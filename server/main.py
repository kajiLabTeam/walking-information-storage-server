from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from PIL import Image
from starlette.requests import Request

from config.const.path import IMAGE_PATH
from domain.models.floor_map.floor_map import FloorMap
from domain.models.tracking_particle.tracking_particle import TrackingParticle
from presentation.handlers.get_particles_floor_map_handler import \
    router as get_image_router
from presentation.handlers.move_particles_handler import \
    router as move_particles_router
from presentation.handlers.reset_particle import \
    router as reset_particle_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(move_particles_router)
app.include_router(get_image_router)
app.include_router(reset_particle_router)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )


if __name__ == "__main__":
    import uvicorn

    floor_image_path = f"{IMAGE_PATH}/floor1.png"
    floor_image = Image.open(floor_image_path)
    floor_map = FloorMap(floor_image)
    tracking_particle = TrackingParticle(floor_map=floor_map)

    uvicorn.run(app, host="0.0.0.0", port=8000)
