class Time(object):
    def __init__(self, hour=0, min=0, sec=0):
        self.hour = hour
        self.min = min
        self.sec = sec

    def __repr__(self):
        return f"Class Time: {self.hour:02d}:{self.min:02d}:{self.sec:02d}"

    def __str__(self):
        return f"{self.hour:02d}:{self.min:02d}:{self.sec:02d}"

    def from_str(self, time):
        time = [int(i) for i in time.split(':')]
        self.hour = time[0]
        self.min = time[1]
        self.sec = time[2]


A = Time(12, 25, 30)

print(A)
print(repr(A))
print(str(A))
print()

B = Time(2, 25, 3)

print(B)
print(repr(B))
print(str(B))
print()

C = Time(2, 25)

print(C)
print(repr(C))
print(str(C))
print()

D = Time()

print(D)
print(repr(D))
print(str(D))
print()

D.from_str("03:09:19")

print(D)
print(repr(D))
print(str(D))
