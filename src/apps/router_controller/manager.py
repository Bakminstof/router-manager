from httpx import AsyncClient

from apps.router_controller.models import WANIPRequestUtils
from apps.router_controller.utils import make_wan_config
from core.settings import Settings


class RouterManger:
    def __init__(
        self,
        wan_name: str,
        wan_ip_request_utils: WANIPRequestUtils,
        timeout: int,
    ) -> None:
        self.wan_ip_request_utils = wan_ip_request_utils
        self.timeout = timeout
        self.wan_name = wan_name

    async def __get_raw_config(self) -> str:
        async with AsyncClient(
            headers=self.wan_ip_request_utils.headers,
            cookies=self.wan_ip_request_utils.cookie,
            params=self.wan_ip_request_utils.params,
            timeout=self.timeout,
            verify=False,
        ) as client:
            response = await client.post(
                url=self.wan_ip_request_utils.url,
                data=self.wan_ip_request_utils.data,
                timeout=self.timeout,
            )

            return response.text

    async def get_wan_ip(self) -> str:
        raw_config = await self.__get_raw_config()
        wan_config = make_wan_config(self.wan_name, raw_config)

        return wan_config.externalIPAddress


def make_router_manager(settings: Settings) -> RouterManger:
    wan_name = settings.router.wan_name
    request_utils = WANIPRequestUtils()
    timeout = settings.request_timeout

    return RouterManger(wan_name, request_utils, timeout)
