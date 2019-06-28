import sys

def bye():
    raise sys.exit(40)       # crucial error: abort now!

try:
    bye()
except:
    print 'got it'           # oops--we ignored the exit
print 'continuing...'

