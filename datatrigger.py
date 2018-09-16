from apscheduler.schedulers.background import BackgroundScheduler

class DataTrigger:
    def __init__(self, function, startAt, stopAt, interval):
        self.function = function
        self.interval = interval
        self.startAt = startAt
        self.stopAt = stopAt

    def setScheduler(self):
        self.sched = BackgroundScheduler()
        hourStr = str(self.startAt) + '-' + str(self.stopAt)
        minuteStr = '*/' + str(self.interval)

        self.sched.add_job(self.function, 'cron', hour = hourStr, minute = minuteStr)
        self.sched.start()

    def changeStartTime(self, startAt):
        self.startAt = startAt

    def changeStopTime(self, stopAt):
        self.stopAt = stopAt

    def changeInterval(self, interval):
        self.interval = interval

    def killScheduler(self):
        self.sched.shutdown()