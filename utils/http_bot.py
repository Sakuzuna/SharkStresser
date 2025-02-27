import time
import random
from utils.client_utils import create_http_client

class HTTPBot:
    def __init__(self, proxy, user_agent, headers=None):
        self.proxy = proxy
        self.user_agent = user_agent
        self.headers = headers or {}
        self.session, self.proxies = create_http_client(proxy, headers)

    def get_request(self, url):
        headers = {"User-Agent": self.user_agent, **self.headers}
        try:
            response = self.session.get(url, headers=headers, proxies=self.proxies)
            return response.status_code
        except Exception as e:
            return str(e)

    def post_request(self, url, data):
        headers = {"User-Agent": self.user_agent, **self.headers}
        try:
            response = self.session.post(url, data=data, headers=headers, proxies=self.proxies)
            return response.status_code
        except Exception as e:
            return str(e)
