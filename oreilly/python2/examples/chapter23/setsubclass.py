class Set(list):
    def __init__(self, value = []):    # constructor
        list.__init__([])              # customizes list
        self.concat(value)             # copies mutable defaults

    def intersect(self, other):        # other is any sequence
        res = []                       # self is the subject
        for x in self:
            if x in other:             # pick common items
                res.append(x)
        return Set(res)                # return a new Set

    def union(self, other):            # other is any sequence
        res = Set(self)                # copy me and my list
        res.concat(other)
        return res

    def concat(self, value):           # value: list, Set...
        for x in value:                # removes duplicates
            if not x in self:
                self.append(x)

    def __and__(self, other): return self.intersect(other)
    def __or__(self, other):  return self.union(other)
    def __repr__(self):       return 'Set:' + list.__repr__(self)

if __name__ == '__main__':
    x = Set([1,3,5,7])
    y = Set([2,1,4,5,6])
    print x, y, len(x)
    print x.intersect(y), y.union(x)
    print x & y, x | y
    x.reverse(); print x
