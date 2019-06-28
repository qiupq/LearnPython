import os, string
if len(sys.argv) == 1:                     # if no filenames are specified,
    filenames = os.listdir(os.curdir)      #   use current dir
else:                                      # otherwise, use files specified
    filenames = sys.argv[1:]               #   on the command line
for filename in filenames:
    if ' ' in filename:
        newfilename = filename.replace(' ', '_')
        print "Renaming", filename, "to", newfilename, "..."
        os.rename(filename, newfilename)
