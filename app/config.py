import os
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BOT_ADMIN = os.getenv("BOT_ADMIN")

BLANK_BUTTONS = {
    "observer": "\U0001F52D Наблюдать",
    "stop": "\U00002715 Остановить"
}

DIALOGUE = {
    "hello_admin": "Приветствую тебе администратор.\nЯ готов наблюдать за появлением товара.",
    "no_admin": "Вы не являетесь администратором.\nУходите от сюда."
}
