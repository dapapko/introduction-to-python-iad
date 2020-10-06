# Task 4
class CollectionIter:
    def __init__(self, collection):
        self.index = -1
        self.collection = collection
        self.itr = iter(collection)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.collection): raise StopIteration
        self.index += 1
        return self.index, next(self.itr)


print("Task #4")
d = ["apple", "banana", "orange"]
for x in CollectionIter(d): print(x)