#!/usr/bin/python
import cgi
form = cgi.FieldStorage()
f1 = form.getfirst('usrname', 'empty')
print """\
Content-Type: text/html\n
<html>
<p>ok! your name will be saved  as %s</p>
</html>
""" %f1