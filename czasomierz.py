import gmaps
import waiter
from datetime import datetime
import time


def disp():
    print(datetime.now(),': ', gmaps.getDrivingTime("Bochenka 25", "50.0441996, 19.9664313"), 'min')

waiter.setScheduler(disp)

while(True):
    # actTime = waiter.waitTillMinutesMul(5)
    # drivingTime = gmaps.getDrivingTime("Bochenka 25", "50.0441996, 19.9664313")
    time.sleep(1)
    