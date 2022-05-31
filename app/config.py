import os
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BOT_ADMIN = os.getenv("BOT_ADMIN")
BLANK_BUTTONS = {
    "filter": "\U00002699 Фильтр",
    "observer": "\U0001F52D Наблюдать",
    "stop": "\U00002715 Остановить",
}
INTERVAL = 1  # min
TASK_NAME = "observer"
API_URL = "https://api-crypto.letmespeak.org/api/escrow"
MARKET_URL = "https://market.letmespeak.org"
PROXIES = os.getenv("PROXIES").replace(" ", "").split(",")  # type: ignore
PROXY_LOGIN = os.getenv("PROXY_LOGIN")
PROXY_PASSWORD = os.getenv("PROXY_PASSWORD")
PROXY_TEST_URL = "http://icanhazip.com/"


DIALOGUE = {
    "intro": f"Следим за NFT персонажами на {MARKET_URL}",
    "hello_admin": "Приветствую тебе администратор.\nЯ помогаю наблюдать за появлением товара.",
    "no_admin": "Вы не являетесь администратором.\nУходите от сюда.",
    "no_filter": "Не указан фильтр, не могу работать",
    "info_filter": f"Перейдите на сайт {MARKET_URL} и отфильтруйте товары по нужным критериям.\n"
                   f"Скопируйте получившейся url и вставьте url сюда",
    "url_success": "URL добавлен, можно наблюдать за товаром",
    "url_fail": "Что-то не так с URL",
    "watch_on": "Начинаю наблюдение",
    "watch_off": "Наблюдение остановлено",
    "watch_process": "Наблюдение уже идет, сначало остановите его",
    "proxy_no_data": "Проверти данные для прокси",
}
