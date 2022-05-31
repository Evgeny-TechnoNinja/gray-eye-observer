import requests
from random import choice
from config import PROXY_TEST_URL  # noqa


class Proxy:
    """
    Builds a proxy in the desired configuration, tests, provides a working proxy for work
    """
    __proxies_data = None
    __attempts = 10
    __TEST_URL = PROXY_TEST_URL
    __timeout = 3

    def __init__(self, proxies: list, login: str, password: str):
        self.proxies = proxies
        self.login = login
        self.password = password

    def __build_proxy(self):
        if len(self.proxies[0]) == 0 or not self.login or not self.password:
            return False
        self.__proxies_data = [f"{self.login}:{self.password}@{proxy}" for proxy in self.proxies]

    def __choose_random_proxy(self):
        if isinstance(self.__proxies_data, bool):
            return False
        else:
            random_proxy = choice(self.__proxies_data)
            blank_proxies = {
                "http": "http://{}".format(random_proxy),
                "https": "http://{}".format(random_proxy)
            }
            return blank_proxies

    def __check_proxies_working(self):
        try:
            proxies = self.__choose_random_proxy()
            if isinstance(proxies, bool):
                return False
            status_code = requests.get(self.__TEST_URL, proxies=proxies, timeout=self.__timeout).status_code
            if status_code != 200:
                raise Exception("Status cod bad")
            return proxies
        except Exception as error:
            print("Error", error)
            if self.__attempts > 0:
                self.__attempts -= 1
                return False

    def get_proxy(self):
        self.__build_proxy()
        proxy = self.__check_proxies_working()
        if isinstance(proxy, bool) and not proxy:
            return False
        return proxy
