import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

# Gmail Credentials
host = "smtp.gmail.com"
port = 587
ssl = 465
username = ""
password = ""
from_email = username
to_list = [""]
try:
    # Connect to host
    email_connect = smtplib.SMTP(host, port)
    # Send Helo
    email_connect.ehlo()
    # Upgrace connection to encrypted
    email_connect.starttls()
    # Login
    try:
        email_connect.login(username, password)
    except smtplib.SMTPAuthenticationError:
        print("Enable login from less secure App on your gmail account")
    # Send email parametters
    the_msg = MIMEMultipart("alternative")
    the_msg['Subject'] = "Greetings!"
    the_msg['From'] = "Simple Test"
    the_msg['To'] = ""
    # Content fo emailt
    plain_txt = "Simple test"
    html_txt = """
    <html>
        <head></head>
        <body>
            <p>Hey!</br>
                We are <b>blablabla</b>, here is the confirmation <a href='https://mbolo1.ddns.net/'>lnk</a>.
            </p>
        </body>
    </html>
    """
    # Set format of emails
    part_1 = MIMEText(plain_txt, 'plain')
    part_2 = MIMEText(html_txt, 'html')
    # Attach content to email message
    the_msg.attach(part_1)
    the_msg.attach(part_2)
    # Send message as string
    email_connect.sendmail(from_email, to_list, the_msg.as_string())
    #Close connection
    email_connect.quit()
except smtplib.SMTPException:
    print("Error sending message")
