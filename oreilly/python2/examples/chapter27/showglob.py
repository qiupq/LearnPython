import sys, glob
print sys.argv[1:]
sys.argv = [item for arg in sys.argv for item in glob.glob(arg)]
print sys.argv[1:]
