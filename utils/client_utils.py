import socket
import requests
from socks import socksocket, PROXY_TYPE_SOCKS4, PROXY_TYPE_SOCKS5

class HttpClient:
    @staticmethod
    def create_session(proxy, user_agent):
        session = requests.Session()
        session.headers.update({"User-Agent": user_agent})
        if proxy:
            session.proxies = {
                "http": f"{proxy['protocol']}://{proxy['host']}:{proxy['port']}",
                "https": f"{proxy['protocol']}://{proxy['host']}:{proxy['port']}",
            }
        return session

class TcpClient:
    @staticmethod
    def create_socket(proxy):
        sock = socksocket()
        if proxy["protocol"] == "socks4":
            sock.set_proxy(PROXY_TYPE_SOCKS4, proxy["host"], proxy["port"])
        elif proxy["protocol"] == "socks5":
            sock.set_proxy(PROXY_TYPE_SOCKS5, proxy["host"], proxy["port"])
        return sock
