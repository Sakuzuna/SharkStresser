import argparse
from banner import sharkprint
from file_loader import load_proxies, load_user_agents
from workers.http_bypass_attack import start_bypass_attack
from workers.http_flood_attack import start_flood_attack

def main():
    print(sharkprint)
    parser = argparse.ArgumentParser(description="Network Stress Testing Tool")
    parser.add_argument("target", help="Target URL or IP")
    parser.add_argument("--method", choices=["http_flood", "http_bypass"], required=True, help="Attack method")
    parser.add_argument("--duration", type=int, default=60, help="Attack duration in seconds")
    parser.add_argument("--packet-size", type=int, default=64, help="Packet size in bytes (for HTTP flood)")
    args = parser.parse_args()

    proxies = load_proxies("data/proxies.txt")
    user_agents = load_user_agents("data/uas.txt")

    if args.method == "http_flood":
        start_flood_attack(args.target, proxies, user_agents, args.duration, args.packet_size)
    elif args.method == "http_bypass":
        start_bypass_attack(args.target, proxies, user_agents, args.duration)

if __name__ == "__main__":
    main()
