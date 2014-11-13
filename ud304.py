#various methods for processing info from the ud304 project 

import re

file = open('index.html', 'r')

doc = str(file.read())
#Task 1 Search for capital html element names, attributes, attribute values



caps = re.findall(r'[A-Z][A-Z]+', doc , re.M )
print "Test 1 found the following words in caps" , caps


#Task 2 find trailing and leading whitespace

leadingWhitespace = re.findall(r'^[ +t]+', doc, re.M)
print "Leading Whitespace at ", leadingWhitespace

trailingWhitespace = re.findall(r'[ \t]+$', doc, re.M)
print "trailing Whitespace at ", trailingWhitespace


#Task 3 HTML Templates do not use UTF-8 as character encoding
encoding = re.findall(r'utf-8', doc, re.I|re.M)
print "encoding check" , encoding

#Task 4 Comments

comments = re.find(r'{<!--}')
