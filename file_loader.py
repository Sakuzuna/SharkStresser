import os
from urllib.parse import urlparse
from utils.client_utils import validate_proxy

def load_proxies(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return []

    with open(file_path, "r") as f:
        proxies = []
        for line in f:
            line = line.strip()
            if line:
                print(f"Processing proxy: {line}")
                parsed = urlparse(line)
                proxy = {
                    "protocol": parsed.scheme,
                    "host": parsed.hostname,
                    "port": parsed.port,
                }
                print(f"Parsed proxy: {proxy}") 
                if validate_proxy(proxy): 
                    print(f"Valid proxy: {proxy}")
                    proxies.append(proxy)
                else:
                    print(f"Invalid proxy: {proxy}") 
        return proxies

def load_user_agents(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return []

    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]
