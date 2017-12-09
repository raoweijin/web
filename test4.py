import cgi, cgitb

import cgi;
import cgitb
cgitb.enable()


form = cgi.FieldStorage()

i=form["age"].value
#print()
print("Status: 200 OK")
print("Content-type: text/html k")
print()

print("<HTMLl>")
print("<HEAD>")
print("<TITLE>Python Sample CGI</TITLE>")
print("</HEAD>")
print("<BODY>")
print("<h1>This is a header</h1>")
#i=9
#i=i*9
print("<p>") #this is a comment
print("Test4: age is  ",i)
print("</p>")
print("</BODY>")
print("</HTML>")
