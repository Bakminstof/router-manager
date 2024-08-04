from fastapi import FastAPI

from apps.router_controller import home_router_manager_router


def register_routers(app: FastAPI) -> None:
    app.include_router(
        home_router_manager_router,
        tags=["Router manager"],
    )
