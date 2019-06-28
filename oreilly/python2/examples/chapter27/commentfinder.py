# Show comment lines (lines that start with a #, like this one)
import sys
for line in sys.stdin:
    if line[0] == '#':
        print line,
