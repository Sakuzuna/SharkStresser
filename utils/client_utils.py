import socket
from urllib.parse import urlparse
from socks import socksocket, PROXY_TYPE_SOCKS4, PROXY_TYPE_SOCKS5

def create_socks_proxy(proxy):
    proxy_type = PROXY_TYPE_SOCKS4 if proxy["protocol"] == "socks4" else PROXY_TYPE_SOCKS5
    sock = socksocket()
    sock.set_proxy(proxy_type, proxy["host"], proxy["port"])
    return sock

def create_http_client(proxy, headers=None):
    import requests
    proxies = {
        "http": f"{proxy['protocol']}://{proxy['host']}:{proxy['port']}",
        "https": f"{proxy['protocol']}://{proxy['host']}:{proxy['port']}",
    }
    session = requests.Session()
    return session, proxies
