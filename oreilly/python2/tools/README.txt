Source-code from the book Programming Python 2nd Edition,
which may be used to convert text files in the distribution
to Unix/Linux or Windows line-terminator formats.  

To use, run the todos.py or tounix.py scripts from this directory
(or double-click on their icons), to convert to DOS and Unix line
terminators, respectively.  No arguments are required.

Directory details in the top-level todos/tounix scripts' code
have been modified slightly for use in this simpler distribution
structure (the original assumed that the fix* scripts were one
level below).  Also, todos/tounix no longer assume python is on
your system path (it uses sys.executable instead).

