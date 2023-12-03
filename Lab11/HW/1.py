class Clock:
    def __init__(self):
        self.hh = 0
        self.mm = 0 
        self.ss = 0  

    def run(self):
        while True:
            self.display_time()
            self.increment_time()

    def increment_time(self):
        self.ss += 1
        if self.ss == 60:
            self.ss = 0
            self.mm += 1
            if self.mm == 60:
                self.mm = 0
                self.hh += 1
                if self.hh == 24:
                    self.hh = 0

    def setTime(self, h, m, s):
        self.hh = h
        self.mm = m
        self.ss = s

    def display_time(self):
        print(f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}")


class AlarmClock(Clock):
    def __init__(self):
        super().__init__()
        self.alarm_hh = 0
        self.alarm_mm = 0
        self.alarm_ss = 0
        self.alarm_on_off = False

    def setAlarmTime(self, h, m, s):
        self.alarm_hh = h
        self.alarm_mm = m
        self.alarm_ss = s

    def alarm_on(self):
        self.alarm_on_off = True

    def alarm_off(self):
        self.alarm_on_off = False

    def run(self):
        while True:
            self.display_time()
            self.display_alarm_time()
            self.increment_time()
            if self.alarm_on_off and self.hh == self.alarm_hh and self.mm == self.alarm_mm and self.ss == self.alarm_ss:
                print("Alarm is going off!")
                break

    def display_alarm_time(self):
        print(f"Alarm Time: {self.alarm_hh:02d}:{self.alarm_mm:02d}:{self.alarm_ss:02d}")


# Example usage:
clock = AlarmClock()
clock.setTime(9, 30, 0)
clock.setAlarmTime(10, 31, 0) 
clock.alarm_on() 
clock.run()  

