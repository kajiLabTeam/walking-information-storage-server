from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.requests import Request

from app.application.errors import ApplicationError
from app.domain.errors import DomainError
from app.infrastructure.errors import InfrastructureError
from app.presentation.handlers import generate_trajectory_router, health_check_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(generate_trajectory_router)
app.include_router(health_check_router)


@app.exception_handler(ApplicationError)
async def application_error_handler(
    _: Request,
    exc: ApplicationError,
) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "type": exc.type.value,
        },
    )


@app.exception_handler(InfrastructureError)
async def infrastructure_error_handler(
    _: Request,
    exc: InfrastructureError,
) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "type": exc.type.value,
        },
    )


@app.exception_handler(DomainError)
async def domain_error_handler(
    _: Request,
    exc: DomainError,
) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "type": exc.type.value,
        },
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(
    _: Request,
    exc: HTTPException,
) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )
