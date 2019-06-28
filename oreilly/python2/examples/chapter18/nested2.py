from nested1 import X, printer    # copy names out
X = 88                            # changes my "X" only!
printer()                         # nested1's X is still 99
