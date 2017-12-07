import cgi, cgitb

import cgi;
import cgitb
cgitb.enable()


form = cgi.FieldStorage()

i=form["email_address"].value
'''
        
#Create instance of FieldStorage
#form = cgi.FieldStorage() 
form = cgi.FieldStorage(environ="post")
cgitb.enable()


#Here I will collect all parameters
variable = ""
value = ""
allFields = ""
for key in form.keys():
    variable = str(key)
    value = str(form.getvalue(variable))
    allFields += variable + ":" + value + "   "

i =allFields

import sys, urllib
#query_string = sys.stdin.read()


multiform = urllib.parse.parse_qs(query_string)
i = multiform["email_address"]

'''
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
print("<p>") #this is a comment
print("See this is just like most other HTML based on python ",i)
print("</p>")
print("</BODY>")
print("</HTML>")