'''This is a course file for ud304 HTML & CSS. The gradinator passes on information to the course file for analysis'''
import webbrowser, os.path
import re
import test_validator
import json
import requests


#Ideally this would be sent from the gradinator
file = open('../sampleProject/index.html', 'r')

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
    output.write('<br>')

#Task 2 find trailing and leading whitespace

    leadingWhitespace = re.findall(r'^[ +t]+', doc, re.M)
    trailingWhitespace = re.findall(r'[ \t]+$', doc, re.M)
    output.write('<h3> Test 2 found the following whitespace: ')
    output.write('Leading Whitespace at')
    output.write(str(leadingWhitespace))
    output.write('Trailing Whitespace at')
    output.write(str(trailingWhitespace))
    output.write('</h3')
    output.write('<br>')


#Task 3 HTML Templates do not use UTF-8 as character encoding
    encoding = re.findall(r'utf-8', doc, re.I|re.M)
    output.write('<h3> Test 3 found the following encoding: ')
    output.write(str(encoding))
    output.write('</h3>')
    output.write('<br>')


#Runs code through the CSS and HTML validator
def match_trailing_whitespace(filename):
    with open(filename) as f:
        # Reads the whole file at once...
        for line in f.read().splitlines():
            if re.search(r"\s+$", line):
                return True
    return False


def match_inconsistent_indentation(filename):
    tab_found = False
    space_found = False
    with open(filename) as f:
        for line in f:
            for match in re.findall(r"^\s+", line):
                if "\t" in match:
                    tab_found = True
                if " " in match:
                    space_found = True
                if tab_found and space_found:
                    return tab_found and space_found
    return tab_found and space_found

#Runs html and css code against validator 
def validate():
    html_check = requests.post(
    "http://validator.w3.org/check",
    data={"output": "json"},
    files={"uploaded_file": ("", doc, 'text/html')}
    )
    
    output.write('<div> - W3C HTML Validator - </div>')
    
    s1 = '<div> HTML: ' + html_check.headers['x-w3c-validator-status'] + '</div>'
    output.write(str(s1))
    
    s2 = '<div> Errors: ' + html_check.headers.get('x-w3c-validator-errors', 0) + '</div>'
    output.write(str(s2))
    
    s3 = '<div> Warnings: ' + html_check.headers.get('x-w3c-validator-warnings', 0) + '</div>'
    output.write(str(s3))
    for error in json.loads(html_check.text).get('messages', []):
        s4 = '<div>' + "[{}] {}".format(error['type'], error['message']) + '</div>'
        output.write(str(s4))

    # css_check = requests.post(
    #     "http://jigsaw.w3.org/css-validator/validator",
    #     data={"output": "json"},
    #     # files={"file": ("file", open("main.css"), 'text/css')}
    #     files={"file": ("file", f_css, 'text/css')}
    # )
    # css_json = json.loads(css_check.text)['cssvalidation']
    # print
    # print '- W3C CSS Validator -'
    # print
    # print 'CSS:', css_check.headers['x-w3c-validator-status']
    # print 'Errors:', css_json['result']['errorcount']
    # for error in css_json.get('errors', []):
    #     print "[{}] {}".format(error['type'], error['message'])
    # print 'Warnings:', css_json['result']['warningcount']
    # for warning in css_json.get('warnings', []):
    #     print "[{}] {}".format(warning['type'], warning['message'])

    
    # output.write('<div> - Miscellaneous (HTML) - </div>') 
    # if match_trailing_whitespace("../sampleProject/index.html"):
    #     print "Trailing whitespace in HTML file."
    # if match_inconsistent_indentation("../sampleProject/index.html"):
    #     print "Inconsistent indentation in HTML file."

    # print
    # print '- Miscellaneous (CSS) -'
    # if match_inconsistent_indentation("main.css"):
    #     print "Inconsistent indentation in CSS file."
    # if match_trailing_whitespace("main.css"):
    #     print "Trailing whitespace in CSS file."



#Puts closing tags on file and launches web page
def render():
    output.write("</body> </html>")
    output.close()
    webbrowser.open("file:///" + os.path.abspath(filename))






    





    


initiateReport()
renderScreens()
styleGuideTest()
validate()
render()




