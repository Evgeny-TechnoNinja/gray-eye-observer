from loader import BOT as bot, KEYBOARD_MAIN_MENU as MAIN_MENU  # noqa
from config import BLANK_BUTTONS, TASK_NAME, INTERVAL, DIALOGUE  # noqa
from utils import observer, Manager  # noqa
import validators


spin = True
watch = False
url = ""


@bot.callback_query_handler(func=lambda call: True)
def callback_inline_keyboard(call):
    global spin, watch, url
    FILTER, OBSERVER, STOP = list(BLANK_BUTTONS.keys())
    manager = Manager(observer, TASK_NAME, INTERVAL)
    if call.data == FILTER:
        def set_url(message):
            global url
            valid_url = validators.url(message.text)
            if valid_url:
                url = message.text
                text = DIALOGUE["url_success"]  # noqa
                bot.send_message(call.from_user.id, text, reply_markup=MAIN_MENU)
            else:
                text = DIALOGUE["url_fail"]  # noqa
                bot.send_message(call.from_user.id, text, reply_markup=MAIN_MENU)

        if not watch:
            text = DIALOGUE["info_filter"]
            bot.send_message(chat_id=call.message.chat.id, text=text)
            bot.register_next_step_handler(call.message, set_url)
        else:
            text = DIALOGUE["watch_process"]
            bot.send_message(call.from_user.id, text, reply_markup=MAIN_MENU)
    if call.data == OBSERVER:
        if not url:
            text = DIALOGUE["no_filter"]
            bot.send_message(call.from_user.id, text, reply_markup=MAIN_MENU)
        else:
            if watch:
                text = DIALOGUE["watch_process"]
                bot.send_message(call.from_user.id, text, reply_markup=MAIN_MENU)
            else:
                print("start watch")
                watch = True
                print("watch", watch)
                text = DIALOGUE["watch_on"]
                bot.send_message(call.from_user.id, text)
                manager.add_url(url)
                manager.create_schedule()
                if not spin:
                    spin = True
                while spin:
                    print("work ...")
                    manager.run()
    if call.data == STOP:
        if not url:
            text = DIALOGUE["no_filter"]
            bot.send_message(call.from_user.id, text, reply_markup=MAIN_MENU)
        else:
            spin = manager.stop()
            watch = False
            text = DIALOGUE["watch_off"]
            bot.send_message(call.from_user.id, text)


