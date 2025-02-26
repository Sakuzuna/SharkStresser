import random
import requests
from socks import socksocket, PROXY_TYPE_SOCKS4, PROXY_TYPE_SOCKS5

class HTTPBot:
    def __init__(self, proxies, user_agents):
        self.proxies = proxies
        self.user_agents = user_agents

    def get_random_proxy(self):
        return random.choice(self.proxies)

    def get_random_user_agent(self):
        return random.choice(self.user_agents)

    def send_request(self, url, payload=None):
        proxy = self.get_random_proxy()
        user_agent = self.get_random_user_agent()

        try:
            session = requests.Session()
            session.proxies = {
                "http": f"{proxy['protocol']}://{proxy['host']}:{proxy['port']}",
                "https": f"{proxy['protocol']}://{proxy['host']}:{proxy['port']}",
            }
            session.headers.update({"User-Agent": user_agent})

            if payload:
                response = session.post(url, data=payload, timeout=5)
            else:
                response = session.get(url, timeout=5)

            if response.status_code < 500:
                print(f"✅ Request to {url} via {proxy['host']}:{proxy['port']} succeeded")
            else:
                print(f"❌ Request to {url} via {proxy['host']}:{proxy['port']} failed")
        except Exception as e:
            print(f"❌ Request to {url} via {proxy['host']}:{proxy['port']} failed")
