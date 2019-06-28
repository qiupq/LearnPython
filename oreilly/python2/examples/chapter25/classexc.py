class General:            pass
class Specific1(General): pass
class Specific2(General): pass

def raiser0():
    X = General()          # raise superclass instance
    raise X

def raiser1():
    X = Specific1()        # raise subclass instance
    raise X

def raiser2():
    X = Specific2()        # raise different subclass instance
    raise X

for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General:        # match General or any subclass of it
        import sys
        print 'caught:', sys.exc_type
