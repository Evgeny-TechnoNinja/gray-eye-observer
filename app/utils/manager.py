import threading
import schedule
from time import sleep


class Manager:
    """
    Create scheduled work execution in a single thread
    """
    __url = ""

    def __init__(self, func, name, interval):
        self.func = func
        self.name = name
        self.interval = interval

    def __create_threading(self, job_func):
        job_thread = threading.Thread(target=job_func, args=(self.__url,))
        job_thread.name = f"thread_{self.name}"
        job_thread.start()

    def add_url(self, url):
        self.__url = url

    def create_schedule(self):
        schedule.every(self.interval).minutes.do(self.__create_threading, self.func).tag(self.name)

    @staticmethod
    def run():
        schedule.run_pending()
        sleep(1)

    def stop(self):
        schedule.clear(self.name)
        return False
