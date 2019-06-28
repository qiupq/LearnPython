import sys, traceback

def safe(entry, *args):
    try:
        apply(entry, args)                 # catch everything else
    except:
        traceback.print_exc()
        print 'Got', sys.exc_type, sys.exc_value

if __name__ == '__main__':
    import oops2
    safe(oops2.oops)
