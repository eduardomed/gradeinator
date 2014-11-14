import json
import re
import requests


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


def validate():
    html_check = requests.post(
    "http://validator.w3.org/check",
    data={"output": "json"},
    files={"uploaded_file": ("", open("../sampleProject/index.html"), 'text/html')}
    # files={"uploaded_file": ("", f_html, 'text/html')}
    )
    print
    print '- W3C HTML Validator -'
    print
    print 'HTML:', html_check.headers['x-w3c-validator-status']
    print 'Errors:', html_check.headers.get('x-w3c-validator-errors', 0)
    print 'Warnings:', html_check.headers.get('x-w3c-validator-warnings', 0)
    for error in json.loads(html_check.text).get('messages', []):
        print "[{}] {}".format(error['type'], error['message'])

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

    print
    print '- Miscellaneous (HTML) -'
    if match_trailing_whitespace("../sampleProject/index.html"):
        print "Trailing whitespace in HTML file."
    if match_inconsistent_indentation("../sampleProject/index.html"):
        print "Inconsistent indentation in HTML file."

    # print
    # print '- Miscellaneous (CSS) -'
    # if match_inconsistent_indentation("main.css"):
    #     print "Inconsistent indentation in CSS file."
    # if match_trailing_whitespace("main.css"):
    #     print "Trailing whitespace in CSS file."
