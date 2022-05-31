from .proxy import Proxy
from config import PROXIES, PROXY_LOGIN, PROXY_PASSWORD  # noqa


def observer(url):
    print(f"work job observer {url}")
    responsible_proxy = Proxy(PROXIES, PROXY_LOGIN, PROXY_PASSWORD)
    proxy = responsible_proxy.get_proxy()
    print("proxy", proxy)


# observer("www.example.com")
