def load_proxies(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def load_user_agents(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]
