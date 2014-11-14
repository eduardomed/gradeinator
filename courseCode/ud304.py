'''This is a course file for ud304 HTML & CSS. The gradinator passes on information to the course file for analysis'''
import webbrowser, os.path, os, shutil, urllib
import re
import fileinput


#Ideally this would be sent from the gradinator

file = open('index.html', 'r')
source = urllib.urlopen('index.html')




doc = str(file.read())


filename='tempBrowseLocal.html'


output = open(filename, 'w')

#Creates HTML file that renders results
def initiateReport():
    
    
    
    contents = '''<!DOCTYPE html>
        <html>
        <head>
        <title>Results </title>
        <script async="" type="text/javascript" src="http://www.gstatic.com/pub-config/ca-pub-2888483682038752.js"></script><script type="text/javascript" async="" src="http://www.google-analytics.com/ga.js"></script><script src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js" type="text/javascript"></script>
        <meta charset="UTF-8">
        <script type="text/javascript">
        var _gaq = _gaq || [];
        _gaq.push(['_setAccount', 'UA-83229-12']);
        _gaq.push(['_trackPageview']);
        
        (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
        })();
        </script>
        </head>
        <body> '''
    output.write(contents)


#Renders original source code
def viewSource():
    output.write('<p>HTML Source Code</p> <div style="width:95%; height:25%; overflow:scroll"><xmp>')
    
    output.write(doc)
    
    output.write('</xmp> </div>')

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
viewSource()
render()




