from functools import cached_property
from os import environ
from pathlib import Path

from pydantic import BaseModel, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent
ENV_DIR = BASE_DIR / "env"

environ.setdefault(
    "ENV_FILE",
    (ENV_DIR / "dev.env").absolute().as_posix(),
)


class RouterSettings(BaseModel):
    host: str = "192.168.1.1"
    protocol: str = "http"

    wan_name: str = "ewan_pppoe"

    auth_token: str

    @computed_field
    @cached_property
    def url(self) -> str:
        return f"{self.protocol}://{self.host}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="app.",
        env_file=(
            f"{ENV_DIR / '.env.template'}",
            f"{ENV_DIR / '.env'}",
            environ["ENV_FILE"],
        ),
        case_sensitive=False,
        env_nested_delimiter=".",
        env_file_encoding="UTF-8",
    )

    # ======================================|Main|====================================== #
    debug: bool

    base_dir: Path = BASE_DIR
    base_encoding: str = "UTF-8"

    api_name: str
    api_version: str

    host: str
    port: int

    request_timeout: int = 10
    # =====================================|Router|===================================== #
    router: RouterSettings


settings = Settings()
