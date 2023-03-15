from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import taxi_fare_router
from api.routes import login


def get_app() -> FastAPI:
    app = FastAPI()
    app.include_router(login.login_router)
    app.include_router(taxi_fare_router.router)
    return app

app = get_app()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
