class Set:
   def __init__(self, value = []):    # constructor
       self.data = []                 # manages a list
       self.concat(value)

   def intersect(self, other):        # other is any sequence
       res = []                       # self is the subject
       for x in self.data:
           if x in other:             # pick common items
               res.append(x)
       return Set(res)                # return a new Set

   def union(self, other):            # other is any sequence
       res = self.data[:]             # copy of my list
       for x in other:                # add items in other
           if not x in res:
               res.append(x)
       return Set(res)

   def concat(self, value):           # value: list, Set...
       for x in value:                # removes duplicates
          if not x in self.data:
               self.data.append(x)

   def __len__(self):          return len(self.data)        # len(self)
   def __getitem__(self, key): return self.data[key]        # self[i]
   def __and__(self, other):   return self.intersect(other) # self & other
   def __or__(self, other):    return self.union(other)     # self | other
   def __repr__(self):         return 'Set:' + `self.data`  # print
