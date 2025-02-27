from urllib.parse import urlparse
from utils.client_utils import validate_proxy

def load_proxies(file_path):
    with open(file_path, "r") as f:
        proxies = []
        for line in f:
            line = line.strip()
            if line:
                parsed = urlparse(line)
                proxy = {
                    "protocol": parsed.scheme,
                    "host": parsed.hostname,
                    "port": parsed.port,
                }
                if validate_proxy(proxy):  
                    proxies.append(proxy)
        return proxies

def load_user_agents(file_path):
    """
    Load user agents from a file.
    """
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]
