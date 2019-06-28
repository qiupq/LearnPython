class Number:
    def __init__(self, start):              # on Number(start)
        self.data = start
    def __sub__(self, other):               # on instance - other
        return Number(self.data - other)    # result is a new instance

