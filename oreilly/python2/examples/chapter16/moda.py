X = 88               # my X: global to this file only

def f():
    global X         # change my X
    X = 99           # cannot see names in other modules
