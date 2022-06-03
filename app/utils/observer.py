from .proxy import Proxy
from config import PROXIES, PROXY_LOGIN, PROXY_PASSWORD, DIALOGUE  # noqa
from .parsing import parsing
from .get_data import get_data
from loader import BOT as bot, KEYBOARD_MAIN_MENU as MAIN_MENU  # noqa


old_total = None


def observer(url, message):
    global old_total
    repeat = 10
    responsible_proxy = Proxy(PROXIES, PROXY_LOGIN, PROXY_PASSWORD)
    proxy = responsible_proxy.get_proxy()
    url_tracking = parsing(url)
    data = get_data(repeat, url_tracking, proxy)
    if not data:
        text = DIALOGUE["watching_fail"]
        bot.send_message(message.from_user.id, text)
    total = data.get("total")
    if old_total is None:
        old_total = total
    # --- dev test
    # We intentionally change the values to
    # check the operation of the notification
    # if old_total == total:
    #     old_total = total + 10
    # ---
    if old_total != total:
        old_total = total
        text = DIALOGUE["changes"].format(url)
        bot.send_message(message.chat.id, text, reply_markup=MAIN_MENU)
