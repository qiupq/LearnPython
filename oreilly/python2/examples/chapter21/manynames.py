X = 11                  # module (global) name/attribute

class c:
    X = 22              # class attribute
    def m(self):
        X = 33          # local variable in method
        self.X = 44     # instance attribute

def f():
    X = 55              # local variable in funtion

def g():
    print X             # access module X (11) 


# Part 2

obj = c()
obj.m()

print obj.X             # 44: instance
print c.X               # 22: class     (a.k.a: obj.X if no X in instance)
print X                 # 11: module    (a.k.a: manynames.X outside file)

#print c.m.X            # FAILS: only visible in method
#print f.X              # FAILS: only visible in function
