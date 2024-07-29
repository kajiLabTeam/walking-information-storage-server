from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from presentation.handlers.finish_walking_handler import router as finish_walking_router
from presentation.handlers.get_particles_floor_map_handler import (
    router as get_image_router,
)
from presentation.handlers.health_check_handler import router as health_check_router
from presentation.handlers.move_pedestrian_handler import (
    router as move_pedestrian_router,
)
from presentation.handlers.start_walking_handler import router as start_walking_router
from starlette.requests import Request

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(get_image_router)
app.include_router(start_walking_router)
app.include_router(finish_walking_router)
app.include_router(move_pedestrian_router)
app.include_router(health_check_router)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )
