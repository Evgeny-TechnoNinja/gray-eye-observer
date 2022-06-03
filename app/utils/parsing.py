from config import API_URL  # noqa


def parsing(url: str) -> str:
    """
    Parses the url to make a usable url for product tracking
    :param url: url from user with filter
    :return: url for tracking
    """
    return f"{API_URL}?{url.split('?')[1]}"

