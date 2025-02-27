import requests
from urllib.parse import urlparse

def validate_proxy(proxy):
    try:
        session = requests.Session()
        session.proxies = {
            "http": f"{proxy['protocol']}://{proxy['host']}:{proxy['port']}",
            "https": f"{proxy['protocol']}://{proxy['host']}:{proxy['port']}",
        }
        print(f"Testing proxy: {proxy}")  
        response = session.get("https://example.com", timeout=5)
        print(f"Proxy response: {response.status_code}")  
        return response.status_code == 200
    except Exception as e:
        print(f"Proxy failed: {e}")  
        return False
        
def create_http_client(proxy, headers=None):
    session = requests.Session()
    proxies = {
        "http": f"{proxy['protocol']}://{proxy['host']}:{proxy['port']}",
        "https": f"{proxy['protocol']}://{proxy['host']}:{proxy['port']}",
    }
    session.proxies = proxies
    return session, proxies
