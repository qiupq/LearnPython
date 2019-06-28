from mytools import Lister            # get tool class

class Super:
    def __init__(self):               # superclass __init__
        self.data1 = "spam"

class Sub(Super, Lister):             # mix-in a __repr__
    def __init__(self):               # Lister has access to self
        Super.__init__(self)
        self.data2 = "eggs"           # more instance attrs
        self.data3 = 42

if __name__ == "__main__":
    X = Sub()
    print X                           # mixed-in repr
