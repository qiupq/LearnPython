class Lister:
    def __repr__(self):
        return ("<Instance of %s(%s), address %s:\n%s>" %
                          (self.__class__.__name__,  # my class's name
                           self.supers(),            # my class's supers
                           id(self),                 # my address
                           self.attrnames()) )       # name=value list
    def attrnames(self):
        result = ''
        for attr in self.__dict__.keys():                # instance namespace dict
            if attr[:2] == '__':
                result = result + "\tname %s=<built-in>\n" % attr
            else:
                result = result + "\tname %s=%s\n" % (attr, self.__dict__ [attr])
        return result

    def supers(self):
        result = ""
        first = 1
        for super in self.__class__.__bases__:   # one level up from class
            if not first:
                result = result + ", "
            first = 0
            result = result + super.__name__     # name, not repr(super) 
        return result


if __name__ == '__main__':
    class Super:
        def __init__(self):               # superclass __init__
            self.data1 = "spam"

    class Sub(Super, Lister):             # mix-in a __repr__
        def __init__(self):               # Lister has access to self
            Super.__init__(self)
            self.data2 = "eggs"           # more instance attrs
            self.data3 = 42

    X = Sub()
    print X                               # mixed-in repr
