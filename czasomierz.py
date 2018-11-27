from gmaps import Gmaps
from datatrigger import DataTrigger
from datetime import datetime
import time


def disp1():
    print(datetime.now(),': ', gmapsClientMorning.getDrivingTime(), 'min (pessimistic: ', gmapsClientMorningPessimist.getDrivingTime(), 'min)')

def disp2():
    print(datetime.now(),': ', gmapsClientAfternoon.getDrivingTime(), 'min (pessimistic: ', gmapsClientAfternoonPessimist.getDrivingTime(), 'min)')

gmapsClientMorning = Gmaps("Bochenka 25", "50.0441996, 19.9664313")
gmapsClientMorningPessimist = Gmaps("Bochenka 25", "50.0441996, 19.9664313", "pessimistic")
gmapsClientAfternoon = Gmaps("50.0441996, 19.9664313", "Bochenka 25")
gmapsClientAfternoonPessimist = Gmaps("50.0441996, 19.9664313", "Bochenka 25", "pessimistic")
triggerMorning = DataTrigger(disp1, 6, 10, 5)
triggerAfternoon = DataTrigger(disp2, 19, 21, 1)

triggerMorning.setScheduler()
triggerAfternoon.setScheduler()

while(True):
    time.sleep(1)
    