from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

from apps.router_controller.manager import make_router_manager
from core.settings import settings

router = APIRouter()
home_router_manager = make_router_manager(settings)


@router.get("/wan_ip", response_class=PlainTextResponse)
async def get_wan_ip():
    return await home_router_manager.get_wan_ip()
