
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

def init():
    scheduler = BackgroundScheduler()
    # scheduler.add_job(func=funcName, trigger='interval', hours=24)
    scheduler.start()

    atexit.register(lambda: scheduler.shutdown())