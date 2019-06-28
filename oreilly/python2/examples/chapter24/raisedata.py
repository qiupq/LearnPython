myException = 'Error'                 # string object

def raiser1():
    raise myException, "hello"        # raise, pass data

def raiser2():
    raise myException                 # raise, None implied

def tryer(func):
    try:
        func()
    except myException, extraInfo:    # run func, catch exception+data
        print 'got this:', extraInfo
