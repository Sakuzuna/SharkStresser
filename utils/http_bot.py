import random
import time
from utils.client_utils import HttpClient

class HTTPBot:
    def __init__(self, proxies, user_agents):
        self.proxies = proxies
        self.user_agents = user_agents
        self.visited_urls = set()

    def get_random_proxy(self):
        return random.choice(self.proxies)

    def get_random_user_agent(self):
        return random.choice(self.user_agents)

    def send_request(self, url):
        proxy = self.get_random_proxy()
        user_agent = self.get_random_user_agent()
        session = HttpClient.create_session(proxy, user_agent)

        try:
            response = session.get(url, timeout=5)
            print(f"🦈 Shark ate a fish: {url} using proxy: {proxy['host']}:{proxy['port']} successful. Nom-Nom")
        except Exception as e:
            print(f"🐟 The fish: {url} escaped the shark using proxy: {proxy['host']}:{proxy['port']}. Go try cathc a dinner!: {e}")
