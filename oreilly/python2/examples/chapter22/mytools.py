###########################################
# Lister can be mixed-in to any class, to
# provide a formatted print of instances
# via inheritance of __repr__ coded here;
# self is the instance of the lowest class;
###########################################

class Lister:
   def __repr__(self):
       return ("<Instance of %s, address %s:\n%s>" %
                         (self.__class__.__name__,      # my class's name
                          id(self),                     # my address
                          self.attrnames()) )           # name=value list
   def attrnames(self):
       result = ''
       for attr in self.__dict__.keys():                # instance namespace dict
           if attr[:2] == '__':
               result = result + "\tname %s=<built-in>\n" % attr
           else:
               result = result + "\tname %s=%s\n" % (attr, self.__dict__ [attr])
       return result
