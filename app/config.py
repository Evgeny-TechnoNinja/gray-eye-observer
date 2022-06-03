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
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
    "Mozilla/5.0 (Android 10; Mobile; rv:81.0) Gecko/81.0 Firefox/81.0"
]

DIALOGUE = {
    "intro": f"Следим за NFT персонажами на {MARKET_URL}",
    "hello_admin": "Приветствую тебя, администратор.\nЯ помогаю наблюдать за появлением товара.",
    "no_admin": "Вы не являетесь администратором.\nУходите от сюда.",
    "no_filter": "Не указан фильтр, не могу работать",
    "info_filter": f"Перейдите на сайт {MARKET_URL} и отфильтруйте товары по нужным критериям.\n"
                   f"Скопируйте получившийся url и вставьте url сюда",
    "url_success": "URL добавлен, можно наблюдать за товаром",
    "url_fail": "Что-то не так с URL",
    "watch_on": "Начинаю наблюдение",
    "watch_off": "Наблюдение остановлено",
    "watch_process": "Наблюдение уже идет, сначала остановите его",
    "proxy_no_data": "Проверьте данные для прокси",
    "watching_fail": "Не могу отследить изменения",
    "changes": "\U000026A0 Есть изменения на странице\n{}\nПродолжаю наблюдениe",
}
