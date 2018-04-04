#! /usr/bin/pyton
import cgi
form = cgi.FieldStorage()
f1 = form.getfirst('username', 'empty')
print """\
<html>
<p>ok! your name will be saved  as %s</p>
""" %f1