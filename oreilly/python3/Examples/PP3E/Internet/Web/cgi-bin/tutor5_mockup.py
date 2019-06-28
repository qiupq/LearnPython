#!/usr/bin/python
##################################################################
# run tutor5 logic with formMockup instead of cgi.FieldStorage()
# to test: python tutor5_mockup.py > temp.html, and open temp.html
##################################################################
     
from formMockup import formMockup
form = formMockup(name='Bob',
                  shoesize='Small',
                  language=['Python', 'C++', 'HTML'], 
                  comment='ni, Ni, NI')
     
# rest same as original, less form assignment

     
import cgi, sys
#form = cgi.FieldStorage()           # parse form data
print "Content-type: text/html"      # plus blank line
     
html = """
<TITLE>tutor5.py</TITLE>
<H1>Greetings</H1>
<HR>
<H4>Your name is %(name)s</H4>
<H4>You wear rather %(shoesize)s shoes</H4>
<H4>Your current job: %(job)s</H4>
<H4>You program in %(language)s</H4>
<H4>You also said:</H4>
<P>%(comment)s</P>
<HR>"""
     
data = {}
for field in ['name', 'shoesize', 'job', 'language', 'comment']:
    if not form.has_key(field):
        data[field] = '(unknown)'
    else:
        if type(form[field]) != type([]):
            data[field] = form[field].value
        else:
            values = map(lambda x: x.value, form[field])
            data[field] = ' and '.join(values)
print html % data

