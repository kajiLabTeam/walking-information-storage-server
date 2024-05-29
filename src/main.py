from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from starlette.requests import Request

from presentation.handlers.get_particles_floor_map_handler import \
    router as get_image_router
from presentation.handlers.move_particles_handler import \
    router as move_particles_router

app = FastAPI()


app.include_router(move_particles_router)
app.include_router(get_image_router)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0")
