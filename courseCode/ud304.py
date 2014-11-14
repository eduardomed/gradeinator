'''This is a course file for ud304 HTML & CSS. The gradinator passes on information to the course file for analysis'''
import webbrowser, os.path
import re


#Ideally this would be sent from the gradinator
file = open('index.html', 'r')

doc = str(file.read())

filename='tempBrowseLocal.html'

output = open(filename,"w")

#Creates HTML file that renders results
def initiateReport():
    
    

    contents = '''<!DOCTYPE html>
    <html>
    <body> '''
    output.write(contents)




#Renders final project in various screen sizes
def renderScreens():

    render = '''<div class="iphone">
        <h2>iPhone Screen</h2>
    <iframe src="index.html" name="iframe_iphone" width = "375" height="667"></iframe>
        </div>
        <div class="ipad">
        <h2> iPad Screen </h2>
        <iframe src="index.html" name="iframe_ipad" width = "1024" height="768"></iframe>
        </div>
        <div class="desktop">
        <h2> Desktop Screen </h2>
        <iframe src="index.html" name="iframe_desktop" width = "1280" height="800"></iframe>
        </div> '''
    output.write(render)



#Tests code against Nanodegree Style Guide
def styleGuideTest():


#Task 1 Search for capital html element names, attributes, attribute values
    caps = re.findall(r'[A-Z][A-Z]+', doc , re.M )
    output.write( '<h3>  Test 1 found the following words in caps')
    output.write(str(caps)),
    output.write('</h3>')

#Task 2 find trailing and leading whitespace

    leadingWhitespace = re.findall(r'^[ +t]+', doc, re.M)
    trailingWhitespace = re.findall(r'[ \t]+$', doc, re.M)
    output.write('<h3> Test 2 found the following whitespace: ')
    output.write('Leading Whitespace at')
    output.write(str(leadingWhitespace))
    output.write('Trailing Whitespace at')
    output.write(str(trailingWhitespace))
    output.write('</h3')


#Task 3 HTML Templates do not use UTF-8 as character encoding
    encoding = re.findall(r'utf-8', doc, re.I|re.M)
    output.write('<h3> Test 3 found the following encoding: ')
    output.write(str(encoding))
    output.write('</h3')



#Puts closing tags on file and launches web page
def render():
    output.write("</body> </html>")
    output.close()
    webbrowser.open("file:///" + os.path.abspath(filename))



    


initiateReport()
renderScreens()
styleGuideTest()
render()




