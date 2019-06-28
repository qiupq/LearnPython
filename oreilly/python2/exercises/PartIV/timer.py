import time
timerfunc = time.clock     # or time.time on some platforms

def timer(reps, func, *args):
    start = timerfunc( )
    for i in xrange(reps):
        apply(func, args)
    return timerfunc( ) – start

