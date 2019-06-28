class C1:
    def meth1(self): self.__X = 88       # now X is mine
    def meth2(self): print self.__X      # becomes _C1__X in I

class C2:
    def metha(self): self.__X = 99       # me too
    def methb(self): print self.__X      # becomes _C2__X in I

class C3(C1, C2): pass
I = C3()                                 # two X names in I

I.meth1(); I.metha()
print I.__dict__
I.meth2(); I.methb()
