from loader import BOT as bot  # noqa
from config import BLANK_BUTTONS, TASK_NAME, INTERVAL  # noqa
from utils import observer, Manager  # noqa

spin = True


@bot.callback_query_handler(func=lambda call: True)
def callback_inline_keyboard(call):
    global spin
    OBSERVER, STOP = list(BLANK_BUTTONS.keys())
    manager = Manager(observer, TASK_NAME, INTERVAL)
    if call.data == OBSERVER:
        manager.create_schedule()
        if not spin:
            spin = True
        while spin:
            manager.run()
    if call.data == STOP:
        spin = manager.stop()

