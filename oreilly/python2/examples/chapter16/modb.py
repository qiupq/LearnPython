X = 11               # my X: global to this file only

import moda          # gain access to names in moda
moda.f()             # sets moda.X, not my X
print X, moda.X
