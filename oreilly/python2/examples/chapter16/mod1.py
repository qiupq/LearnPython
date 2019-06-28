X = 1
import mod2

print X,                    # my global X
print mod2.X,               # mod2's X
print mod2.mod3.X           # nested mod3's X
