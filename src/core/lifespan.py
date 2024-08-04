from contextlib import AbstractAsyncContextManager, asynccontextmanager
from typing import Self

from fastapi import FastAPI

from core.routers import register_routers


class Lifespan:
    async def on_startup(self, app: FastAPI) -> None:
        register_routers(app)

    async def on_shutdown(self) -> None:
        pass

    @asynccontextmanager
    async def __call__(self, app: FastAPI) -> AbstractAsyncContextManager[Self]:
        await self.on_startup(app)
        yield
        await self.on_shutdown()

    async def __aenter__(self, app: FastAPI) -> Self:
        await self.on_startup(app)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.on_shutdown()
