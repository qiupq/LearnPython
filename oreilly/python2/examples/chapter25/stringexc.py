General   = 'general'
Specific1 = 'specific1'
Specific2 = 'specific2'

def raiser0(): raise General
def raiser1(): raise Specific1
def raiser2(): raise Specific2

for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except (General, Specific1, Specific2):     # catch any of these 
        import sys
        print 'caught:', sys.exc_type
