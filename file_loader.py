from urllib.parse import urlparse

def load_proxies(file_path):
    with open(file_path, "r") as f:
        proxies = []
        for line in f:
            line = line.strip()
            if line:
                parsed = urlparse(line)
                proxies.append({
                    "protocol": parsed.scheme,
                    "host": parsed.hostname,
                    "port": parsed.port,
                })
        return proxies

def load_user_agents(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]
