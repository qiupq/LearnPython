class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop  = stop
    def __iter__(self):                   # get iterator object
        return self
    def next(self):                       # on each for iteration
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2
