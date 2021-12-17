
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

from app.configs.scheduler.email_report_job import send_email_report

def init():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=send_email_report, trigger='interval', hours=2)
    scheduler.start()

    atexit.register(lambda: scheduler.shutdown())