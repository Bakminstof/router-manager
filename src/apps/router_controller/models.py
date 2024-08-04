from pydantic import BaseModel, field_validator
from pydantic_core.core_schema import ValidationInfo

from core.settings import settings


class WANIPRequestUtils(BaseModel):
    url: str = f"{settings.router.url}/cgi"

    headers: dict[str, str] = {
        "Accept": "*/*",
        "Accept-Language": "ru-RU,ru;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "text/plain",
        "Origin": settings.router.url,
        "Pragma": "no-cache",
        "Referer": f"{settings.router.url}/mainFrame.htm",
        "X-KL-Ajax-Request": "Ajax_Request",
    }

    cookie: dict[str, str] = {"Authorization": f"Basic {settings.router.auth_token}"}

    params: tuple[tuple[str, str], ...] = (
        ("1", ""),
        ("1", ""),
        ("1", ""),
        ("5", ""),
        ("5", ""),
        ("5", ""),
        ("5", ""),
        ("5", ""),
        ("5", ""),
        ("5", ""),
    )

    data: str = (
        "[SYS_MODE#0,0,0,0,0,0#0,0,0,0,0,0]0,1\r\n"
        "mode\r\n"
        "[IGD#0,0,0,0,0,0#0,0,0,0,0,0]1,1\r\n"
        "LANDeviceNumberOfEntries\r\n"
        "[IGD_DEV_INFO#0,0,0,0,0,0#0,0,0,0,0,0]2,3\r\n"
        "softwareVersion\r\n"
        "hardwareVersion\r\n"
        "upTime\r\n"
        "[WAN_COMMON_INTF_CFG#0,0,0,0,0,0#0,0,0,0,0,0]3,1\r\n"
        "WANAccessType\r\n"
        "[WAN_IP_CONN#0,0,0,0,0,0#0,0,0,0,0,0]4,0\r\n"
        "[WAN_PPP_CONN#0,0,0,0,0,0#0,0,0,0,0,0]5,0\r\n"
        "[WAN_L2TP_CONN#0,0,0,0,0,0#0,0,0,0,0,0]6,0\r\n"
        "[WAN_PPTP_CONN#0,0,0,0,0,0#0,0,0,0,0,0]7,0\r\n"
        "[L2_BRIDGING_ENTRY#0,0,0,0,0,0#0,0,0,0,0,0]8,1\r\n"
        "bridgeName\r\n"
        "[LAN_WLAN#0,0,0,0,0,0#0,0,0,0,0,0]9,12\r\n"
        "status\r\n"
        "SSID\r\n"
        "BSSID\r\n"
        "channel\r\n"
        "autoChannelEnable\r\n"
        "standard\r\n"
        "beaconType\r\n"
        "basicEncryptionModes\r\n"
        "X_TP_Bandwidth\r\n"
        "possibleDataTransmitRates\r\n"
        "WPAAuthenticationMode\r\n"
        "IEEE11iAuthenticationMode\r\n"
    )


class WANConfig(BaseModel):
    enable: bool
    connectionStatus: str
    possibleConnectionTypes: str
    connectionType: str
    PPPoESessionID: int
    defaultGateway: str
    name: str
    uptime: int
    lastConnectionError: str
    idleDisconnectTime: int
    RSIPAvailable: bool
    NATEnabled: bool
    X_TP_FullconeNATEnabled: bool
    X_TP_FirewallEnabled: bool
    X_TP_IGMPProxyEnabled: bool
    X_TP_IGMPForceVersion: str
    username: str
    password: str
    PPPAuthenticationProtocol: str
    X_TP_IfName: str
    X_TP_L2IfName: str
    X_TP_BcastAddr: str
    X_TP_ConnectionId: int
    X_TP_UseStaticIP: bool
    externalIPAddress: str
    remoteIPAddress: str
    maxMRUSize: int
    currentMRUSize: int
    DNSEnabled: bool
    DNSOverrideAllowed: bool
    DNSServers: list[str]
    MACAddress: str
    MACAddressOverride: str
    X_TP_ClonedMACAddress: str
    transportType: str
    PPPoEACName: str
    PPPoEServiceName: str
    connectionTrigger: str
    routeProtocolRx: str
    PPPLCPEcho: bool
    PPPLCPEchoRetry: int
    X_TP_IPv4Enabled: bool
    X_TP_IPv6Enabled: bool
    X_TP_IPv6ConnStatus: str
    X_TP_IPv6CPUp: bool
    X_TP_IPv6AddressingType: str
    X_TP_ExternalIPv6Address: str
    X_TP_PrefixLength: int
    X_TP_DefaultIPv6Gateway: str
    X_TP_DefaultIPv6GatewayOverride: str
    X_TP_IPv6DNSEnabled: bool
    X_TP_IPv6DNSOverrideAllowed: bool
    X_TP_IPv6DNSServers: str
    X_TP_PDEnabled: bool
    X_TP_SitePrefix: str
    X_TP_SitePrefixLength: int
    X_TP_SitePrefixPltime: int
    X_TP_SitePrefixVltime: int
    X_TP_DSLiteEnabled: bool
    portMappingNumberOfEntries: int
    secondConnection: str

    @field_validator("DNSServers", mode="before")
    def dns_servers_validator(
        cls,
        value: str,
        info: ValidationInfo,
        **kwargs,
    ):
        return value.split(",")
