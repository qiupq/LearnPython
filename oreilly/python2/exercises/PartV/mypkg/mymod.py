def countLines(name):
    file = open(name, 'r')
    return len(file.readlines())

def countChars(name):
    return len(open(name, 'r').read())            # defaults to 'r'

def test(name):                                   # Or pass file object
    return countLines(name), countChars(name)     # Or return a dictionary
