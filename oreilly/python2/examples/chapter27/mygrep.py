import fileinput, sys, string
# take the first argument out of sys.argv and assign it to searchterm
searchterm, sys.argv[1:] = sys.argv[1], sys.argv[2:]
for line in fileinput.input():
   num_matches = line.count(searchterm)
   if num_matches:                     # a nonzero count means there was a match
       print "found '%s' %d times in %s on line %d." % (searchterm, num_matches, 
           fileinput.filename(), fileinput.filelineno())
