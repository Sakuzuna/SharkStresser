def load_proxies(file_path):
    with open(file_path, "r") as file:
        lines = file.read().splitlines()
    proxies = []
    for line in lines:
        if not line or line.startswith("#"):
            continue
        protocol, rest = line.split("://")
        if "@" in rest:  
            auth, host_port = rest.split("@")
            username, password = auth.split(":")
            host, port = host_port.split(":")
        else:  
            host, port = rest.split(":")
            username, password = None, None
        proxies.append({
            "protocol": protocol,
            "host": host,
            "port": int(port),
            "username": username,
            "password": password,
        })
    return proxies
