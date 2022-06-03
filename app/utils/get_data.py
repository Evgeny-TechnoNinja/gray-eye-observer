import requests
from config import USER_AGENTS  # noqa
from random import choice
from time import sleep


def get_data(repeat, url, proxy):
    """
    Provides data obtained from a link
    :param repeat: retries request  on failure
    :param url: url with data
    :param proxy: ip address in the correct format
    :return: object with data otherwise False
    """
    session = requests.Session()
    session.headers.update({"User-Agent": choice(USER_AGENTS)})
    try:
        data = session.get(url, proxies=proxy)
        if data.status_code != 200:
            raise Exception(f"Status code bad {data.status_code}")
    except Exception as error:
        print("Error", error)
        if repeat > 0:
            sleep(3)
            return get_data(repeat - 1, url, proxy)
        else:
            return False
    return data.json()

