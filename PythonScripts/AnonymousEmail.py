#! /usr/bin/python3

import mechanize
from signal import signal, SIGINT
from sys import exit

# Header
header = """[[YELLOW]]
 #############################################
 ############## ANONYMOUS EMAIL ##############
 #############################################

 The Script will an anonymous email to the
 specified Email address. By Nzanoa.[[NC]]
 eg. [[LPURPLE]]python3 AnonymousEmail.py[[NC]]
"""

# Colors
COLORS = {
    'NC': '\033[0m',
    'RED': '\033[1;31m',
    'GREEN': '\033[0;32m',
    'BLUE': '\033[0;34m',
    'YELLOW': '\033[1;33m',
    'LPURPLE': '\033[1;35m'
}

# Replace color by ANSI COLOR CODE
def ColorText(text):
    for color in COLORS:
        text = text.replace('[[' + color + ']]', COLORS[color])
    return text

# Handle signal
def handler(signal_received, frame):
    # Handle any cleanup here
    signal_error = "\n [-][[RED]] Exiting gracefully [[NC]]\n"
    print(ColorText(signal_error))
    exit(0)

signal(SIGINT, handler)

# Print Header
print(ColorText(header))

# def anonymouse():
br = mechanize.Browser()
# Recipient
input_recipient = " [+][[BLUE]] Enter the recipient Email> [[NC]]"
recipient = input("{}".format(ColorText(input_recipient)))
# Subject
input_subject = " [+][[BLUE]] Enter the Subject > [[NC]]"
subject = input("{}".format(ColorText(input_subject)))
# Message
input_message = " [+][[BLUE]] Enter your message > [[NC]]"
message = input("{}".format(ColorText(input_message)))

# Proxy
url = "http://anonymouse.org/anonemail.html"
headers = "Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)"
br.addheaders = [('User-agent', headers)]
# Build Header
try:
    br.open(url)
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_debug_http(False)
    br.set_debug_redirects(False)
    br.select_form(nr=0)
    br.form['to'] = recipient
    br.form['subject'] = subject
    br.form['text'] = message
    # Submit form
    result = br.submit()
    check_submit = " [+][[GREEN]] Trying to send email...[[NC]]"
    print(ColorText(check_submit))
except:
    fail_submit = " [-][[RED]] Error sending the email[[NC]]\n"
    print(ColorText(fail_submit))

# Getting response back
response = br.response().read()

# Chech if successfull
keywords = "The e-mail has been sent"

try:
    if keywords in response:
        check_response = " [+][[GREEN]] Mail has been recived![[NC]]"
        print(ColorText(check_response))
except:
    fail_response = " [-][[RED]] An error occured[[NC]]\n"
    print(ColorText(fail_response))

# anonymouse()
