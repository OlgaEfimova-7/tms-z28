from datetime import datetime, timedelta


class MyTime:
    def __init__(self, a=None, b=None, c=None):
        if a and type(a) is str:
            list1 = a.split(':')
            self.hours = int(list1[0])
            self.minutes = int(list1[1])
            self.seconds = int(list1[2])
        elif a and b and c:
            self.hours = a
            self.minutes = b
            self.seconds = c
        elif isinstance(a, MyTime):
            self.hours = a.hours
            self.minutes = a.minutes
            self.seconds = a.seconds
        elif not a:
            now = datetime.now()
            self.hours = int(now.strftime('%H'))
            self.minutes = int(now.strftime('%M'))
            self.seconds = int(now.strftime('%S'))
        else:
            print('Wrong input!')

    def __eq__(self, other):
        return (self.hours == other.hours and
                self.minutes == other.minutes and
                self.seconds == other.seconds)

    def __ne__(self, other):
        return (self.hours != other.hours or
                self.minutes != other.minutes or
                self.seconds != other.seconds)

    def __ge__(self, other):
        sec1 = self.hours * 3600 + self.minutes * 60 + self.seconds
        sec2 = other.hours * 3600 + other.minutes * 60 + other.seconds
        return sec1 >= sec2

    def __le__(self, other):
        sec1 = self.hours * 3600 + self.minutes * 60 + self.seconds
        sec2 = other.hours * 3600 + other.minutes * 60 + other.seconds
        return sec1 <= sec2

    def __lt__(self, other):
        sec1 = self.hours * 3600 + self.minutes * 60 + self.seconds
        sec2 = other.hours * 3600 + other.minutes * 60 + other.seconds
        return sec1 < sec2

    def __gt__(self, other):
        sec1 = self.hours * 3600 + self.minutes * 60 + self.seconds
        sec2 = other.hours * 3600 + other.minutes * 60 + other.seconds
        return sec1 > sec2

    def __add__(self, other):
        return (self.hours + other.hours,
                self.minutes + other.minutes,
                self.seconds + other.seconds)

    def __sub__(self, other):
        return (self.hours - other.hours,
                self.minutes - other.minutes,
                self.seconds - other.seconds)

    def __mul__(self, number):
        return (self.hours * number,
                self.minutes * number,
                self.seconds * number)

    def __str__(self):
        sec = self.hours * 3600 + self.minutes * 60 + self.seconds
        return str(timedelta(seconds=sec))


time1 = MyTime(11, 11, 50)
time2 = MyTime('11:10:50')
time3 = MyTime(time1)
time4 = MyTime()
print(time2.seconds, time1.seconds)
print(time1 == time2)
print(time1 != time2)
print(time1 + time2)
print(time1 - time2)
print(time1*5)
print(time1)
print(time3)
print(time4)
print(time1 <= time2)
print(time1 >= time2)
print(time1 < time2)
print(time1 > time2)
