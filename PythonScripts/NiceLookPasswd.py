#! /bin/python

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
                print("{}: {}".format(fields[n], 'encrypted'))
            else:
                #print "%s: %s" % (fields[n], parts[n])
                print("{}: {}".format(fields[n], parts[n]))
        print("\n")

passwd.close()
