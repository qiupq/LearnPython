#!/usr/bin/python
#######################################################
# runs on the server, reads form input, prints html;
# url=http://server-name/cgi-bin/tutor3.py
#######################################################
     
import cgi
form = cgi.FieldStorage()            # parse form data
print "Content-type: text/html"      # plus blank line
     
html = """
<TITLE>tutor3.py</TITLE>
<H1>Greetings</H1>
<HR>
<P>%s</P>
<HR>"""
     
if not form.has_key('user'):
    print html % "Who are you?"
else:
    print html % ("Hello, %s." % form['user'].value)
