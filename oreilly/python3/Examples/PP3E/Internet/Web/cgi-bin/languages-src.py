#!/usr/bin/python
#################################################################
# Display languages.py script code without running it.
#################################################################
     
import cgi
filename = 'cgi-bin/languages.py'
     
print "Content-type: text/html\n"       # wrap up in html
print "<TITLE>Languages</TITLE>"
print "<H1>Source code: '%s'</H1>" % filename
print '<HR><PRE>' 
print cgi.escape(open(filename).read())
print '</PRE><HR>' 
