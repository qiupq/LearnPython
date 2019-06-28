def countLines(name):
    file = open(name, 'r')
    return len(file.readlines())

def countChars(name):
    return len(open(name, 'r').read())

def test(name):                                      # Or pass file object
    return countLines(name), countChars(name)        # Or return a dictionary

if __name__ == '__main__':
    print test('mymod.py')                           # Or sys.argv argument
