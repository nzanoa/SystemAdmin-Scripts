#! /usr/bin/python3

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from signal import signal, SIGINT
from getpass import getpass

# Header
header = """[[YELLOW]]
 #############################################
 ############## SEND HTML EMAIL ##############
 #############################################

 The Script will use a Gmail account to send
 a short HTML Email to the specified Email
 address. By Nzanoa.[[NC]]
 eg. [[LPURPLE]]python3 SendHTMLGmail.py[[NC]]
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
# Gmail Credentials
host = "smtp.gmail.com"
port = 587
ssl = 465
# Email
input_username = " [+][[BLUE]] Enter your Email > [[NC]]"
username = input("{}".format(ColorText(input_username)))
# Password
input_password = " [+][[BLUE]] Enter your password > [[NC]]"
password = getpass("{}".format(ColorText(input_password)))

# Recipient
input_recipient = " [+][[BLUE]] Enter the recipient > [[NC]]"
recipient = input("{}".format(ColorText(input_recipient)))
# Subject
input_subject = " [+][[BLUE]] Enter the Subject > [[NC]]"
subject = input("{}".format(ColorText(input_subject)))
# Message
input_message = " [+][[BLUE]] Enter your message > [[NC]]"
message = input("{}".format(ColorText(input_message)))
from_email = username

try:
    # Connect to host
    email_connect = smtplib.SMTP(host, port)
    # Send Helo
    email_connect.ehlo()
    # Upgrace connection to encrypted
    email_connect.starttls()
    check_connected = " [+][[GREEN]] Successfully Connected[[NC]]"
    print(ColorText(check_connected))
    # Login
    try:
        email_connect.login(username, password)
        check_loggedin = " [+][[GREEN]] Successfully Logged In[[NC]]"
        print(ColorText(check_loggedin))
    except smtplib.SMTPAuthenticationError:
        auth_fail = " [-] Please, Enable [[RED]]Login from less secure App[[NC]]\n     feautre on Gmail"
        print(ColorText(auth_fail))

    # Send email parametters
    the_msg = MIMEMultipart("alternative")
    the_msg['Subject'] = subject
    the_msg['From'] = from_email
    the_msg['To'] = recipient
    # Content fo emailt
    # plain_txt = "Simple test"
    html_txt = """
    <html>
        <head></head>
        <body>
            <p>Hey!</br>
                {}.
            </p>
        </body>
    </html>
    """.format(message)

    # Set format of emails
    # part_1 = MIMEText(plain_txt, 'plain')
    part_2 = MIMEText(html_txt, 'html')
    # Attach content to email message
    # the_msg.attach(part_1)
    the_msg.attach(part_2)
    # Send message as string
    email_connect.sendmail(from_email, recipient, the_msg.as_string())
    check_sent = " [+][[GREEN]] Email Successfully Sent[[NC]]"
    print(ColorText(check_sent))
    #Close connection
    email_connect.quit()
    check_loggedout = " [+][[GREEN]] Logging out...[[NC]]\n"
    print(ColorText(check_loggedout))
except smtplib.SMTPException:
    fail_sending = " [-][[RED]] Error sending the message[[NC]]\n"
    print(ColorText(fail_sending))
