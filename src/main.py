from fastapi import FastAPI

from core.lifespan import Lifespan
from core.settings import settings

app = FastAPI(
    debug=settings.debug,
    title=settings.api_name,
    version=settings.api_version,
    lifespan=Lifespan(),
)


if __name__ == "__main__":
    if settings.debug:
        import uvicorn

        uvicorn.run(
            app="main:app",
            host=settings.host,
            port=settings.port,
            reload=True,
        )
