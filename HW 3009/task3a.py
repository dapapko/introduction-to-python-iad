class FloatIter:
    def __init__(self, start=1.2, stop=5.8, step=0.5):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __str__(self):
        return str(self.start)

    def __next__(self):
        if self.start > self.stop:
            raise StopIteration
        self.start += self.step
        return self


print("Task #3A")
for a in FloatIter():
    print(a)