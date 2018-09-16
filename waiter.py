from datetime import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers import cron



def waitTillMinutesMul(minutes, resolution=5):
    """ Czeka do pełnej wielokrotnoci czasu podanego jako argument "minutes" """
    czas = datetime.now()
    minutesLast = czas.minute

    while(True):
        if czas.minute%minutes == 0 and czas.minute != minutesLast:
            return czas
        else:
            time.sleep(resolution)
            czas = datetime.now()


def setScheduler(fun):
    sched = BackgroundScheduler()
    sched.add_job(fun, 'cron', hour = '14-15', minute = '*/5')
    sched.start()
