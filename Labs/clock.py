class Time(object):
    def __init__(self, hour=0, min=0, sec=0):
        self.hour = hour
        self.min = min
        self.sec = sec

    def __repr__(self):
        return f"Class Time: {self.hour}:{self.min}:{self.sec}"

    def from_str(self, time):
        time = [int(i) for i in time.split(':')]
        self.hour = time[0]
        self.min = time[1]
        self.sec = time[2]
