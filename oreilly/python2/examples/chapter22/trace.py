class wrapper:
    def __init__(self, object):
        self.wrapped = object                        # save object
    def __getattr__(self, attrname):
        print 'Trace:', attrname                     # trace fetch
        return getattr(self.wrapped, attrname)       # delegate fetch
