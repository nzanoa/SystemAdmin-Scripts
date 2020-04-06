#! /bin/python
# Colors
COLORS = {
    'NC': '\033[0m',
    'RED': '\033[1;31m',
    'GREEN': '\033[0;32m',
    'BLUE': '\033[0;34m',
    'YELLOW': '\033[1;33m',
    'LPURPLE': '\033[1;35m'
}

# Header
header = """[[YELLOW]]
 ##############################################
 ############## NICE LOOK PASSWD ##############
 ##############################################

 The Script does not take any argument.
 Gives a nice/easy to understand look
 ot the file /etc/passwd. By Nzanoa.[[NC]]
 eg. [[LPURPLE]]python3 NiceLookPassword.py[[NC]]

"""
# Replace color by ANSI COLOR CODE
def ColorText(text):
    for color in COLORS:
        text = text.replace('[[' + color + ']]', COLORS[color])
    return text

print(ColorText(header))
try:
    # Load /etc/passwd
    filename = '/etc/passwd'
    passwd = open(filename, 'r')

    fields = { 0: "Username", 1: "Password", 2: "User-ID", 3: "Group-ID", 4: "Comments", 5: "Home-Dir", 6: "Shell" }

    for line in passwd:
        parts = line.strip().split(':')

        if parts[6] == '/usr/sbin/nologin' or parts[6] == '/bin/false' or parts[6] == '/sbin/nologin' or parts[6] == '/bin/sync':
            continue
        else:
            for n in range(7):
                if n == 1 and parts[n] == 'x':
                    output = " [[BLUE]]{}[[NC]]: [[GREEN]]{}[[NC]]".format(fields[n], 'encrypted')
                    print(ColorText(output))
                else:
                    output = " [[BLUE]]{}[[NC]]: [[GREEN]]{}[[NC]]".format(fields[n], parts[n])
                    print(ColorText(output))
            print("\r")

    passwd.close()
    last_output = "[[YELLOW]]Done !!![[NC]]"
    print(ColorText(last_output))
except:
    error = "[[RED]]Something went wrong !!![[NC]]"
    print(error)
