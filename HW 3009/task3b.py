# Task 3B

import datetime

class TimeIter:
    def __init__(self, start='20:30:45', hours=1, minutes=0, seconds=0, fmt='%H:%M:%S', max_iter=10):
        self.fmt = fmt
        self.start = datetime.datetime.strptime(start, self.fmt)
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.max_iter = max_iter
        self.iter = 0

    def __iter__(self):
        return self

    def __str__(self):
        return self.start.strftime(self.fmt)

    def __next__(self):
        if self.iter == self.max_iter:
            raise StopIteration
        self.start += datetime.timedelta(hours=self.hours, minutes=self.minutes, seconds=self.seconds)
        self.iter += 1
        return self


print("Task #3B")

for x in TimeIter(max_iter=5):
    print(x)