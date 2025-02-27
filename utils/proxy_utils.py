def normalize_proxy(proxy):
    if "://" not in proxy:
        proxy = "http://" + proxy
    parsed = urlparse(proxy)
    return {
        "protocol": parsed.scheme,
        "host": parsed.hostname,
        "port": parsed.port or (8080 if parsed.scheme == "http" else 1080),
    }

def filter_proxies(proxies, protocol):
    return [p for p in proxies if p["protocol"] == protocol]
