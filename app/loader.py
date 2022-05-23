import telebot
from config import TELEGRAM_TOKEN, BLANK_BUTTONS
from keyboard import create_inline_keyboard as keyboard


BOT = telebot.TeleBot(TELEGRAM_TOKEN)
KEYBOARD_MAIN_MENU = keyboard(BLANK_BUTTONS)
