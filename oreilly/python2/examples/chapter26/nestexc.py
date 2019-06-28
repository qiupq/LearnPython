def action2():
    print 1 + []           # generate TypeError

def action1():
    try:
        action2()
    except TypeError:      # most recent matching try
        print 'inner try'

try:
    action1()
except TypeError:          # here only if action1 reraises
    print 'outer try'
