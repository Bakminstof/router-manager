from re import search

from apps.router_controller.models import WANConfig


def make_wan_config(wan_name: str, data: str) -> WANConfig:
    wan_ppp_conn_section = _get_config_section(wan_name, data)
    attrs = _extract_config_attrs(wan_ppp_conn_section)

    return WANConfig.model_validate(attrs)


def _get_config_section(wan_name: str, data: str) -> str:
    section = search(
        rf"(?<=\[\d,\d,\d,\d,\d,\d]\d\n)[^]]+name={wan_name}[^\[]+",
        data,
    )
    return section.group()


def _extract_config_attrs(config_section: str) -> dict[str, str]:
    attrs = {}

    for line in config_section.strip().split("\n"):
        name, value = line.split("=")

        attrs[name] = value

    return attrs
