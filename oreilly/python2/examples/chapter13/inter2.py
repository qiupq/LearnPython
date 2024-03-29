def intersect(*args):
    res = []
    for x in args[0]:                  # scan first sequence
        for other in args[1:]:         # for all other args
            if x not in other: break   # item in each one?
        else:                          # no:  break out of loop
            res.append(x)              # yes: add items to end
    return res

def union(*args):
    res = []
    for seq in args:                   # for all args
        for x in seq:                  # for all nodes
            if not x in res:
                res.append(x)          # add new items to result
    return res
