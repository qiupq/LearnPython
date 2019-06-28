# a module that lists the namespaces of other modules

verbose = 1

def listing(module):
    if verbose:
        print "-"*30
        print "name:", module.__name__, "file:", module.__file__
        print "-"*30

    count = 0
    for attr in module.__dict__.keys():      # scan namespace
        print "%02d) %s" % (count, attr),
        if attr[0:2] == "__":
            print "<built-in name>"          # skip __file__, etc.
        else:
            print getattr(module, attr)      # same as .__dict__[attr]
        count = count+1

    if verbose:
        print "-"*30
        print module.__name__, "has %d names" % count
        print "-"*30

if __name__ == "__main__":
    import mydir
    listing(mydir)      # self-test code: list myself
