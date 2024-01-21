import os
import random
import string
import time
import math
import threading
from mysql import connector
from time import sleep


mydb = connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    port=3307,
    database='system'
)

cursor = mydb.cursor()
cursor.execute("select * from servers")
servers = cursor.fetchall()
#cursor.execute("insert into servers values('123')")
mydb.commit()

insertIcon = '>'
directoryIcon = ''

"""
import random

def generate_random_ip():
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return ip

# Generowanie 30 losowych adresów IP
for _ in range(30):
    random_ip = generate_random_ip()
    print(random_ip)"""
"""
import random
import string


def generate_random_company_name():
    vowels = "aeiou"
    consonants = "".join(set(string.ascii_lowercase) - set(vowels))

    name = ""
    for _ in range(random.randint(2, 4)):
        name += random.choice(consonants)
        name += random.choice(vowels)

    return name.capitalize() + " Corp"


# Generowanie 30 losowych nazw firm
for _ in range(30):
    random_company_name = generate_random_company_name()
    print(random_company_name)"""

"""import random
import string


def generate_random_credentials():
    login_length = 8
    password_length = 10

    login = ''.join(random.choices(string.ascii_letters + string.digits, k=login_length))
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))

    return login, password


# Generowanie 30 losowych loginów i haseł
for _ in range(30):
    login, password = generate_random_credentials()
    password = '"' + password + '",'
    print(password)"""

"""cursor.execute("update servers set login = null, password = null where ip = '74.153.61.52'")
cursor.execute("update servers set login = null, password = null where ip = '49.159.20.255'")
mydb.commit()"""

cursor.execute("select login ,password from servers where ip = '74.153.61.52'")
p = cursor.fetchone()
cursor.execute("select login ,password from servers where ip = '49.159.20.255'")
e = cursor.fetchone()

if p[0] == e[0] == None and p[1] == e[1] == None:
    login = input("Set login for your PC and your e-mail: ")
    password = input("Set password for your PC and your e-mail: ")
    cursor.execute("update servers set login = (%s), password = (%s) where ip = '74.153.61.52'", (login, password))
    cursor.execute("update servers set login = (%s), password = (%s) where ip = '49.159.20.255'", (login, password))
    print("Login and password has been set")
    mydb.commit()


def countdown_timer(seconds):
    end_time = time.time() + seconds

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        #input("try: ")
        #print(f"Time remaining: {remaining_time} seconds")
        sleep(1)

    print("Time's up!")


def do_something():
    # Perform actions while the timer is running
    while True:
        user_input = input("Enter something (or 'quit' to stop): ")
        if user_input.lower() == 'quit':
            break
        print(f"You entered: {user_input}")


""

ips = ['74.153.61.52', '49.159.20.255', '10.201.88.116', '220.167.246.14', '131.221.70.133', '38.123.58.8', '15.189.82.250', '244.29.72.54', '4.50.249.25', '168.179.39.31', '91.38.200.160', '172.202.224.67', '74.134.18.62', '254.66.179.55', '136.2.51.56', '9.189.216.221', '208.17.140.121', '1.152.90.248', '209.221.237.218', '166.63.187.188', '254.240.145.46', '82.173.77.194', '226.151.126.178', '113.14.41.13', '214.60.113.99', '244.99.104.57', '38.244.221.16', '97.56.19.118', '223.148.117.201', '77.109.234.26', '213.89.156.72', '47.613.36.1']  # 30 + 2(players pc, email) len=32
names = ['Players PC', 'Email', 'Yawi Corp', 'Koka Corp', 'Yefexu Corp', 'Luqojaze Corp', 'Tumu Corp', 'Leso Corp', 'Vazoza Corp', 'Xupu Corp', 'Kuzezu Corp', 'Satu Corp', '"Visu Corp', 'Volazice Corp', 'Diwemove Corp', 'Wuya Corp', 'Duhu Corp', 'Peyikoqu Corp', 'Cunakiya Corp', 'Pihisabu Corp', 'Koxigibe Corp', 'Geluqo Corp', 'Lugoneca Corp', 'Bawolo Corp', 'Cunomana Corp', 'Toya Corp', 'Kagunesi Corp', 'Qiriyu Corp', 'Wapuwila Corp', 'Gecebipu Corp', 'Xetivu Corp', 'Xota Corp']  # 30 + 2(players pc, email) len=30
oprfcs = [4, 4, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]  # 2*4 7*1 10*2 8*3 5*4 len=30+2
sshs = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]  # 30 len=32
ftps = [True, True, None, None, None, None, None, None, None, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]  # 23 len=32
smtps = [True, True, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, True, True, True, True, True, True, True, True, True, True, True, True, True]  # 13 len=32
https = [True, True, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, True, True, True, True, True]  # 5 len=32
proxys = [True, True, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, True, True, True, True, True, True, True, True, True, True, True, True, True, True]  # 14 len=32
firewalls = [True, True, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, True, True, True, True, True, True, True]  # 7 len=32
logins = ['', '', 'I2blnKYA', 'YO1ac2pn', 'Ya22Jikf', '7q2eLbXh', 'Xpa1RgF3', 'C8uqQaxD', 'aMlbNUcd', '3U0bfs19', 'BbKZzrQo', 'ndvavCh5', 'V4FtfqCL', 'b6gUOp4m', 'PV5hkMHS', 'yOFM3VRO', 'ihP7g0ry', '45kqXpzq', 'XNqnW5Ym', 'fD2ehlfh', 'wB00tyj8', 'i4kZnYfV', 'zEn2Hb1I', 'GJ6ZoZPT', 'Z6qkq93J', 'il2ZqVZW', 'ihw8Yaar', 'hav1mjb7', 'SnBq8LQB', 'KqoZOGbY', 'Gcd3IOJk', 'w4HHAzLc']  # 30 + 2(players pc, email) len=32
passwords = ['', '', 'Lb>[UUXWo5', 'L4)!_}>7:o', 'd)C&%yu@3Z', 'rJb0fVtv$G', 'Jr=9<)^P--', '(/5Mje3eA>', 'zutX"[(u5C', '`oo1=U]7]H', 'V6l`]@Akmh', '7UF6/IfO!]', 'Qm-4gXWqI&', 'c,r!y<&&MR', 'G7|)Ys>~/]', 'd816C[]uVO', 'jiO(dea_eL', '6^$m;sZQbP', 'q2U?EMV#[N', 'j0ij;hd5b*', '~G[%s~sC^8', 'w]3`3hdW*>', 'dp8L;UvZYx', '-Ek`{O,sQZ', 'iL#mx|(@$l', 'E,q2\m4]ez', 'RuX9}lhJ;I', 'Mwt\:L9~*f', '%m$!0j4zT;', '5`+8\.\,x9', 'pK.3GGf<sb', 'MDsUQAlr1y']  # 30 + 2(players pc, email) len=32
pwdaquired = [True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]  # len=32
firewalllvl = [6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6]
firewallpwd = ['MzmgnP', 'iAsdOj', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,'BtjCkw', 'jNipuF', 'cgByPV', 'zmxqSK', 'XiBzlQ', 'xmboDg', 'opnNzW']  # 20/6 len=32
"""for i in range(32):
    cursor.execute("insert into servers values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (ips[i], names[i], oprfcs[i], sshs[i], ftps[i], smtps[i], https[i], proxys[i], firewalls[i], logins[i], passwords[i], pwdaquired[i], True, firewalllvl[i], firewallpwd[i]))
mydb.commit()"""
"""for i in range(32):
    cursor.execute("update servers set connected = FALSE where ip != (%s)", (ips[0], ))
mydb.commit()"""
sshcrack = ['ip', 'SSHCrack', 'path', 'exe', '10101011111110101111000100010100001011001111111111110110100011100100111001101101011010000011011111110100011101100111011110011110101001000110101110001111011101101111111010011111010111101110000011111001111101011110011101000011011011100011001001100101110010010111010110100000011000000110111011101011111100011111110010111110011001010110011001111110001010101001110011111110101101100010101010101011100111101111101000011100011100011101101010110111111000']
ftpbounce = ['ip', 'FTPBounce', 'path', 'exe', '1111001011010010000111000101110010101101001110010110000111010111011101100101100110101101111000111101110011111100111100110110011101000011001001010100110101101011110011110100011110000111001011011011101010111110011101100101000101011111011010010111111101110101110101001000001110001010010011110011111001000110111101100001110101000111001111100000110100111100001011101110000001100000110001110100001011001100111111011010000101110011101001110111011100101']
smtpoverflow = ['ip', 'SMTPoverflow', 'path', 'exe', '1110110110001010101010000111100111100010001100100111100011100101111100110111010111000000011010010110010001010100101100110101101100100101000101101100110100100110111111001011001001101100001001101101100011101100100000111000011111111001100101111010011010001111101111011010010010111111001100011010101101100010110010011010101101010010000011011110010000100100101010111011110111101011010100110001011100100111101010101110001011111011101111110111011']
webserverworm = ['ip', 'WebServerWorm', 'path', 'exe', '100100011110111101111001010110101110100010111011100111110110001101011000111001011111011101111011110000001100010111011000011111110011110010001010110110000011100111110010001011111100101110110110101010000111110111010100100001001000101011111110111011110011101101100010111001101101010010011011110111110010110000101100110101110101001010010001000100010011010110111100000111110010110100111000011111011111000101100111110111101000101011']
hackingFiles = [sshcrack, ftpbounce, smtpoverflow, webserverworm]
"""for i in hackingFiles:
    cursor.execute("insert into files values(%s, %s, %s, %s, %s)", (i[0], i[1], i[2], i[3], i[4]))
    mydb.commit()"""

serverIndex = [10,11,12,13,15,16,17,18,20,23]
secondServerIndex = [13,29,27,23,21,24,14,28,26,19]
rest = [1,2,3,4,5,6,7,8,9,10,11,12,15,16,17,18,20,22,25,30,31]

#  tree
patterns = ["help", "scp {} {}", "scp {}", "scan", "rm {}", "ls", "cd {}", "cd", "mv {} {}", "connect {}", "probe", "exe", "disconnect", "dc", "cat {}", "reboot", "replace {} '{}' '{}'", "analyze", "solve {}", "login", "upload {}", "clear", "append {} {}", "shell", "overload", "sshcrack {}", "ftpbounce {}", "smtpoverflow {}", "webserverworm {}", "porthack {}", "quit", "nano {}", "mkdir {}", "rmdir {}"]
lengths = [1, 3, 2, 1, 2, 1, 2, 1, 3, 2, 1, 1, 1, 1, 2, 1, 4, 1, 2, 1, 2, 1, 3, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2]
commands = ["help", "scp", "scp", "scan", "rm", "ls", "cd", "cd", "mv", "connect", "probe", "exe", "disconnect", "dc", "cat", "reboot", "replace", "analyze", "solve", "login", "upload", "clear", "append", "shell", "overload", "sshcrack", "ftpbounce", "smtpoverflow", "webserverworm", "porthack", "quit", "nano", "mkdir", "rmdir"]
definitions = ["displays all commands", "Copies file named [filename] from remote machine to specified local folder (/bin default)", "Copies file named [filename] from remote machine to specified local folder (/bin default)", "Scans for links on the connected machine and adds them to the list", "Deletes specified file(s)", "Shows all folders and files in current directory", "Moves current working directory to the specified folder", "Moves current working directory to the main folder", "Moves [FILE] to [DESTINATION]", "Connect to an External Computer", "Scans the connected machine for active ports and security level", "Lists all available executables in the local /bin/ folder", "Terminate the current open connection", "Terminate the current open connection", "Displays contents of file", "Reboots the connected computer", "Replaces the target text in the file with the replacement", "Performs an analysis pass on the firewall of the target machine", "Attempts to solve the firewall of the target machine to allow UDP Traffic", "Requests a username and password to log in to the connected system", "Uploads the indicated file on your local machine to the current directory", "Clears the terminal", "Appends a line containing [DATA] to [FILENAME]", "Opens a remote access shell on target machine with Proxy overload and IP trap capabilities", "Uses accessed shells to overload Proxy", "Uses 'SSHCrack.exe' on specified port", "Uses 'FTPBounce.exe' on specified port", "Uses 'SMTPoverflow.exe' on specified port", "Uses 'WebServerWorm.exe' on specified port", "Starts hacking selected port", "Quit the program", "Create new file", "Create new directory", "Remove directory"]
""

currentPath = ''
currentLvl = 0
"""cursor.execute("update servers set connected = False where ip = (%s)", (ips[10], ))
mydb.commit()
cursor.execute("update servers set connected = TRUE where ip = (%s)", (ips[0], ))
mydb.commit()"""
"""cursor.execute("insert into files values('74.153.61.52', 'testing', '/home', 'exe')")
mydb.commit()"""
cursor.execute("update servers set connected = True where ip = (%s)", (ips[0], ))
mydb.commit()


"""def tree():
    cursor.execute("select ip from servers where connected = True")
    ip = cursor.fetchone()[0]
    cursor.execute("select * from folders where ip = %s", (ip, ))
    folders = cursor.fetchall()
    cursor.execute("select * from files where ip = %s", (ip, ))
    files = cursor.fetchall()
    maxLvl = 0
    foldersLvl = []
    spaces = "   "
    foldersinmain = []
    printed = []

    for fo in folders:
        if fo[3] > maxLvl:
            maxLvl = fo[3]

    path = ''
    for fo in folders:
        for i in range(maxLvl + 2):
            if fo[3] == i:
                parts = str(fo[2]).split('/')
                if i != 0 and i < 2:
                    path = '/' + parts[i]
                    #print(path)
                elif i >= 2 and i < len(parts):
                    path = path + '/' + parts[i]
                    #print(path)
                if str(fo[2]) == path:
                    foldersLvl.append(fo)
                    if str(fo[2]) == '':
                        foldersinmain.append(fo)
                    #print(fo)

    path = ''
    for fo in foldersinmain:
        print(fo[1])
        for i in range(maxLvl+1):
            for f in folders:
                parts = str(f[2]).split('/')
                if i != 0 and i < 2 and i < len(parts):
                    path = '/' + parts[i]
                elif i > 1 and i < len(parts):
                    path = path + '/' + parts[i]
                if f[3] != 0 and printed.__contains__(f) == False:
                    if f[2] == fo[1] and f[3] == i:
                        print(f"|{spaces * f[3]}| {f[1]}")
                        printed.append(f)
                    elif '/'+parts[1] == fo[1]:
                        print(f"|{spaces * f[3]}| {f[1]}")
                        printed.append(f)
    
    for fo in folders:
        if fo[0] == ip and fo[3] == 0:
            print('| ' + fo[1])
            for fl in files:
                if fl[0] == ip and fl[2] == fo[1]:
                    print('|   | ' + fl[1] + '.' + fl[3])"""


#tree()


def rmdir(directoryname):
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    cursor.execute("select * from folders where ip = %s and path = %s", (serverIp, currentPath))
    folders = cursor.fetchall()
    exists = False
    for fo in folders:
        if fo[1] == directoryname and fo[2] == currentPath:
            exists = True
            cursor.execute("delete from folders where ip = (%s) and name = (%s) and path = (%s)", (serverIp, directoryname, currentPath))
            mydb.commit()
            print(f"Directory '{directoryname}' has been deleted")
            break
    if exists == False:
        print(f"Directory '{directoryname}' does not exist")


def mkdir(directoryname):
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    cursor.execute("select * from folders where ip = %s and path = %s", (serverIp, currentPath))
    folders = cursor.fetchall()
    exists = False
    for fo in folders:
        if fo[1] == directoryname and fo[2] == currentPath:
            print(f"Directory named {directoryname} already exists in {currentPath}")
            exists = True
            break

    if exists == False:
        cursor.execute("insert into folders values(%s, %s, %s, %s)", (serverIp, directoryname, currentPath, currentLvl))
        mydb.commit()
        print(f"Directory {directoryname} created")


def mail():  # dokoncz
    cursor.execute("select * from messages")
    mail = cursor.fetchall()
    columns = ["Sender", "Title", "Message", "Attachments", "Date", "Time", "Complete?"]
    if len(mail) == 0:
        print("| Sender | Title | Message | Attachments | Date | Time | Complete?")
    else:
        spacesTable = []  # spaces for first row(type of info definition)
        spacesRest = []
        maxlen = [0,0,0,0,0,0,0]
        completed = []

        for m in mail:
            if m[6] == False:
                completed.append("no")
                if maxlen[6] < 2:
                    maxlen[6] = 2
            else:
                completed.append("yes")
                if maxlen[6] < 3:
                    maxlen[6] = 3

        for m in mail:
            for i in range(7):
                if m[i] != None:
                    if len(str(m[i])) > maxlen[i] and i != 4 and i != 5:
                        if len(str(m[i])) > 30:
                            maxlen[i] = len(str(m[i][0:30]))
                        else:
                            maxlen[i] = len(str(m[i]))
                    elif len(str(m[i])) > maxlen[i] and (i == 4 or i == 5):
                        maxlen[i] = len(str(m[i]))
                else:
                    maxlen[i] = len(columns[3])

        for m in range(len(mail)):
            spacesRest.append([])

        index = 0
        for m in mail:
            for i in range(7):
                if m[i] != None:
                    if len(str(m[i])) == maxlen[i]:
                        spacesRest[index].append(1)
                    else:
                        if i != 4 and i != 5 and i != 6:
                            space = maxlen[i] - len(str(m[i][0:30])) + 1
                            spacesRest[index].append(space)
                        elif i == 6:
                            space = len(columns[6]) - len(completed[index]) + 1
                            spacesRest[index].append(space)
                        else:
                            space = maxlen[i] - len(str(m[i])) + 1
                            spacesRest[index].append(space)
                else:
                    spacesRest[index].append(maxlen[i] - len("None") + 1)

            index+=1

        for i in range(len(maxlen)):
            if len(columns[i]) == maxlen[i]:
                spacesTable.append(" ")
            else:
                space = maxlen[i] - len(columns[i]) + 1
                spacesTable.append(" " * space)

        print(f"| Nr | {columns[0]}{spacesTable[0]}| {columns[1]}{spacesTable[1]}| {columns[2]}{spacesTable[2]}| {columns[3]}{spacesTable[3]}| {columns[4]}{spacesTable[4]}| {columns[5]}{spacesTable[5]}| {columns[6]}{spacesTable[6]} |")
        for m in range(len(mail)):
            space = " " * (2-len(str(m)))
            print(f"| {m+1}{space} | {mail[m][0]}{' ' * spacesRest[m][0]}| {mail[m][1]}{' ' * spacesRest[m][1]}| {mail[m][2][0:27] + '...'}{' ' * spacesRest[m][2]}| {mail[m][3]}{' ' * spacesRest[m][3]}| {mail[m][4]}{' ' * spacesRest[m][4]}| {mail[m][5]}{' ' * spacesRest[m][5]}| {completed[m]}{' ' * spacesRest[m][6]}|")

        options = True
        while options:
            inp = str(input("\nInsert '1' to read a message\nInsert '2' to reply to message\nInsert '3' to close mail window: "))
            if inp == "1":
                good = False
                while not good:
                    inp2 = input("\nWhich one?(number): ")
                    try:
                        inp2 = int(inp2)
                        good = True
                    except ValueError:
                        print("\nInteger expected")
                if inp2 in range(len(mail) + 1) and inp2 != 0:
                    print("\nFrom: " + mail[inp2-1][0]+"\nTitle: "+mail[inp2-1][1])
                    parts = str(mail[inp2-1][2]).split()
                    maxl = 50
                    lines = ""
                    ind = 0
                    #print(len(parts))
                    write = True
                    while write:
                        if len(lines) < maxl and ind < len(parts):
                            lines += (parts[ind] + " ")
                            ind+=1
                        elif len(lines) >= maxl and ind < len(parts):
                            lines += "\n"
                            maxl = maxl + 50
                        else:
                            write = False
                    print(lines)

            #if inp == "2":
            cursor.execute("select command from tasks where nr = 1")
            c = cursor.fetchall()[0]
            cursor.execute(c[0])
            s = cursor.fetchall()
            print(s)
            """ok = False
            for f in s:
                if f == False:
                    print("T")
                else:
                    print(f)"""


def nano(filename):
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    cursor.execute("select * from files where ip = (%s)", (serverIp, ))
    files = cursor.fetchall()
    for f in files:
        if f[1] + '.' + f[3] == filename and f[2] == currentPath:
            error = True
            break
        else:
            error = False
    if error == True:
        print(f"File '{filename}' already exists in '{currentPath}'")
    else:
        if str(filename).__contains__('.'):
            parts = str(filename).split('.')
            if parts[1] == "exe":
                print("You cannot write 'exe' files")
            elif parts[1] == "txt" or parts[1] == "docx":
                print(filename)
                content = str(input("Content: "))
                cursor.execute("insert into files values(%s, %s, %s, %s, %s)", (serverIp, parts[0], currentPath, parts[1], content))
                mydb.commit()
                print(f"Created {filename} file")
        else:
            print("File has to have an extension 'txt' or 'docx'")
    return True


def quit():
    cursor.execute("update servers set logged = False, connected = False")
    mydb.commit()
    print("Exiting program in:")
    for i in reversed(range(3)):
        print(i+1)
        sleep(1)
    exit(0)


def porthack(port):
    cursor.execute("select ssh, ftp, smtp, http, oprfc from servers where connected = True")
    securities = cursor.fetchone()
    cursor.execute("select * from hackedports")
    ports = cursor.fetchall()
    success = False
    openedPorts = 0
    for s in securities:
        if s == False:
            openedPorts += 1
        if openedPorts >= securities[4] and success == False:
            for p in ports:
                if str(p[0]) == str(port):
                    if p[1] == False:
                        print(f"Hacking port '{port}' ...")
                        sleep(5)
                        print(f"Successfully hacked port {port}")
                        success = True
                        cursor.execute("update hackedports set hacked = True where name = (%s)", (port, ))
                        mydb.commit()
                        break
                    elif p[1] == True:
                        success = True
                        print(f"Port {port} has already been hacked")
        else:
            if securities[4] == 1:
                word = 'port'
            else:
                word = 'ports'
            print(f"You have to open at least {securities[4]} {word} to hack")
            break


def webserverworm(port):
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    cursor.execute("select http from servers where connected = True")
    http = cursor.fetchone()[0]
    cursor.execute("select * from files where ip = %s", (ips[0], ))
    file = cursor.fetchall()
    fileFound = False
    for f in file:
        if f[1] + '.' + f[3] == 'WebServerWorm.exe':
            fileFound = True
            break
    if fileFound == False:
        print("File 'WebServerWorm.exe' not found")
    elif port == '80' and http == True:
        print("App: Apache Web Server Worm")
        sleep(14)
        cursor.execute("update servers set http = False where ip = (%s)", (serverIp,))
        mydb.commit()
        print("Success")
    elif port == '80' and http == False:
        print("'HTTP' not detected")
    else:
        print("Incorrect port name")


def smtpoverflow(port):
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    cursor.execute("select smtp from servers where connected = True")
    smtp = cursor.fetchone()[0]
    cursor.execute("select * from files where ip = %s", (ips[0], ))
    file = cursor.fetchall()
    fileFound = False
    for f in file:
        if f[1] + '.' + f[3] == 'SMTPoverflow.exe':
            fileFound = True
            break
    if fileFound == False:
        print("File 'SMTPoverflow.exe' not found")
    elif port == '25' and smtp == True:
        print("SMTP Mail Server Overflow")
        sleep(11)
        cursor.execute("update servers set smtp = False where ip = (%s)", (serverIp,))
        mydb.commit()
        print("Success")
    elif port == '25' and smtp == False:
        print("'SMTP Mail Server' not detected")
    else:
        print("Incorrect port name")


def ftpbounce(port):
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    cursor.execute("select ftp from servers where connected = True")
    ftp = cursor.fetchone()[0]
    cursor.execute("select * from files where ip = %s", (ips[0], ))
    file = cursor.fetchall()
    fileFound = False
    for f in file:
        if f[1] + '.' + f[3] == 'FTPBounce.exe':
            fileFound = True
            break
    if fileFound == False:
        print("File 'FTPBounce.exe' not found")
    elif port == '21' and ftp == True:
        print("Working ...")
        sleep(8)
        cursor.execute("update servers set ftp = False where ip = (%s)", (serverIp,))
        mydb.commit()
        print("Success")
    elif port == '21' and ftp == False:
        print("'FTP' not detected")
    else:
        print("Incorrect port name")


def sshcrack(port):
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    cursor.execute("select ssh from servers where connected = True")
    ssh = cursor.fetchone()[0]
    cursor.execute("select proxy, firewall from servers where connected = True")
    proxy, firewall = cursor.fetchone()
    if firewall == True and proxy == True:
        print("Firewall and proxy are active\n")
    elif firewall == True and proxy == False:
        print("Firewall is active")
    elif firewall == False and proxy == True:
        print("Proxy is active")
    else:
        cursor.execute("select * from files where ip = %s", (ips[0], ))
        file = cursor.fetchall()
        fileFound = False
        for f in file:
            if f[1] + '.' + f[3] == 'SSHCrack.exe':
                fileFound = True
                break
        if fileFound == False:
            print("File 'SSHCrack.exe' not found")
        elif port == '22' and ssh == True:
            print("SecureShellCrack Running ...")
            sleep(5)
            cursor.execute("update servers set ssh = False where ip = (%s)", (serverIp,))
            mydb.commit()
            print("SecureShellCrack Completed")
        elif port == '22' and ssh == False:
            print("'SSH' not detected")
        else:
            print("Incorrect port name")


def overload():
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    cursor.execute("select count(*) from shells where active = True")
    shells = cursor.fetchone()[0]
    cursor.execute("select proxy from servers where ip = (%s)", (serverIp, ))
    proxy = cursor.fetchone()[0]
    #print(shells)
    if proxy == True:
        if shells != 0:
            time = 30
            sleep(time/math.sqrt(shells))
            cursor.execute("update shells set active = False")
            mydb.commit()
            cursor.execute("update servers set proxy = False where ip = (%s)", (serverIp, ))
            mydb.commit()
            print("Proxy defeated")
        else:
            print("You have activated 0 shells. Needed at least 1 shell to overload")
    else:
        print("Proxy undetected")


def shell():
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    cursor.execute("select * from shells")
    shells = cursor.fetchall()
    for s in shells:
        if s[0] == serverIp:
            if s[1] == False:
                cursor.execute("update shells set active = True where ip = (%s)", (serverIp, ))
                mydb.commit()
                print("Shell activated")
            else:
                print("Shell has already been activated")


def append(newcontent, filename):
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    cursor.execute("select * from files where ip = (%s) and path = (%s)", (serverIp, currentPath))
    file = cursor.fetchall()
    success = False
    for i in file:
        if i[1] + '.' + i[3] == filename:
            content = i[4] + str(newcontent)
            cursor.execute("update files set content = (%s) where name = (%s) and extension = (%s) and path = (%s)", (content, i[1], i[3], currentPath))
            mydb.commit()
            success = True
            break
    if success == True:
        print(f"Appended {filename} file")
    else:
        print(f"Cannot append {filename} file")


def clear():
    os.system('cls')


def upload(filename):
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    playerPcIp = ips[0]
    success = False
    if serverIp == playerPcIp:
        print("Cannot upload file to your own computer")
    else:
        cursor.execute("select * from files where ip = (%s)", (playerPcIp, ))
        file = cursor.fetchall()
        for i in file:
            if i[1] + '.' + i[3] == filename:
                cursor.execute("insert into files values(%s, %s, %s, %s, %s)", (serverIp, i[1], currentPath, i[3], i[4]))
                mydb.commit()
                success = True
                break
        if success == True:
            print(f"Uploaded {filename} file to {currentPath}")
        else:
            print("Something went wrong")


def login():  # popraw
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    cursor.execute("select pwdaquired from servers where connected = True")
    havepassword = cursor.fetchone()[0]
    cursor.execute("select login from servers where connected = True")
    log = cursor.fetchone()[0]
    cursor.execute("select password from servers where connected = True")
    passw = cursor.fetchone()[0]
    if havepassword == True:
        print(f"Login: {log}, password: {passw}")
    index = 0
    for i in ips:
        if i == serverIp:
            break
        else:
            index+=1
    login = str(input("Login: "))
    password = str(input("Password: "))
    if login == logins[index] and password == passwords[index]:
        cursor.execute("update servers set logged=True where ip = (%s)", (serverIp, ))
        mydb.commit()
        print("Logged in")
        return True
    else:
        print("Incorrect 'login' and/or 'password'")
        return False


def solve(password):
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    index = 0
    for i in ips:
        if i == serverIp:
            break
        else:
            index += 1
    if firewalls[index] == False:
        print("Firewall not detected")
    else:
        cursor.execute("select firewallpwd from servers where ip = (%s)", (serverIp,))
        pwd = cursor.fetchone()[0]
        if password == pwd:
            sleep(1)
            print("Firewall solved")
            cursor.execute("update servers set firewall = False where ip = (%s)", (serverIp, ))
            mydb.commit()
        else:
            sleep(1)
            print("Incorrect password")


def generateRandomString(length):  # used in analyze()
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def analyze():
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    index = 0
    for i in ips:
        if i == serverIp:
            break
        else:
            index+=1
    if firewalls[index] == False:
        print("Firewall not detected")
    else:
        cursor.execute("select firewalllvl from servers where ip = (%s)", (serverIp, ))
        lvl = cursor.fetchone()[0]
        print("Analyzing firewall pattern ...")
        sleep(3)
        if lvl == 6:
            lvl-=1
            for letter in firewallpwd[index]:
                numOfPlaceholders = 20
                replaceIndex = random.randint(0, numOfPlaceholders - 1)
                randomLetters = [generateRandomString(1) for _ in range(numOfPlaceholders)]
                randomLetters[replaceIndex] = letter
                formatedText = ''.join(randomLetters)
                text = ''
                for l in formatedText:
                    text = text + ' ' + l
                print(text)
            cursor.execute("update servers set firewalllvl = (%s) where ip = (%s)", (lvl, serverIp))
            mydb.commit()

        elif lvl == 5:
            lvl-=1
            for letter in firewallpwd[index]:
                numOfPlaceholders = 20
                replaceIndex = random.randint(0, numOfPlaceholders - 1)
                zeroIndex = []
                while len(zeroIndex) < 3:
                    ind = random.randint(0, numOfPlaceholders - 1)
                    if len(zeroIndex) == 0 and ind != replaceIndex:
                        zeroIndex.append(ind)
                    elif zeroIndex.__contains__(ind) == False and ind != replaceIndex:
                        zeroIndex.append(ind)
                randomValues = []
                for i in range(numOfPlaceholders):
                    if i == replaceIndex:
                        randomValues.append(letter)
                    elif i in zeroIndex:
                        randomValues.append('0')
                    else:
                        randomValues.append(generateRandomString(1))
                formatedText = ''.join(randomValues)
                text = ''
                for l in formatedText:
                    text = text + ' ' + l
                print(text)
            cursor.execute("update servers set firewalllvl = (%s) where ip = (%s)", (lvl, serverIp))
            mydb.commit()

        elif lvl == 4:
            lvl -= 1
            for letter in firewallpwd[index]:
                numOfPlaceholders = 20
                replaceIndex = random.randint(0, numOfPlaceholders - 1)
                zeroIndex = []
                while len(zeroIndex) < 6:
                    ind = random.randint(0, numOfPlaceholders - 1)
                    if len(zeroIndex) == 0 and ind != replaceIndex:
                        zeroIndex.append(ind)
                    elif zeroIndex.__contains__(ind) == False and ind != replaceIndex:
                        zeroIndex.append(ind)
                randomValues = []
                for i in range(numOfPlaceholders):
                    if i == replaceIndex:
                        randomValues.append(letter)
                    elif i in zeroIndex:
                        randomValues.append('0')
                    else:
                        randomValues.append(generateRandomString(1))
                formatedText = ''.join(randomValues)
                text = ''
                for l in formatedText:
                    text = text + ' ' + l
                print(text)
            cursor.execute("update servers set firewalllvl = (%s) where ip = (%s)", (lvl, serverIp))
            mydb.commit()

        elif lvl == 3:
            lvl -= 1
            for letter in firewallpwd[index]:
                numOfPlaceholders = 20
                replaceIndex = random.randint(0, numOfPlaceholders - 1)
                zeroIndex = []
                while len(zeroIndex) < 9:
                    ind = random.randint(0, numOfPlaceholders - 1)
                    if len(zeroIndex) == 0 and ind != replaceIndex:
                        zeroIndex.append(ind)
                    elif zeroIndex.__contains__(ind) == False and ind != replaceIndex:
                        zeroIndex.append(ind)
                randomValues = []
                for i in range(numOfPlaceholders):
                    if i == replaceIndex:
                        randomValues.append(letter)
                    elif i in zeroIndex:
                        randomValues.append('0')
                    else:
                        randomValues.append(generateRandomString(1))
                formatedText = ''.join(randomValues)
                text = ''
                for l in formatedText:
                    text = text + ' ' + l
                print(text)
            cursor.execute("update servers set firewalllvl = (%s) where ip = (%s)", (lvl, serverIp))
            mydb.commit()

        elif lvl == 2:
            lvl -= 1
            for letter in firewallpwd[index]:
                numOfPlaceholders = 20
                replaceIndex = random.randint(0, numOfPlaceholders - 1)
                zeroIndex = []
                while len(zeroIndex) < 12:
                    ind = random.randint(0, numOfPlaceholders - 1)
                    if len(zeroIndex) == 0 and ind != replaceIndex:
                        zeroIndex.append(ind)
                    elif zeroIndex.__contains__(ind) == False and ind != replaceIndex:
                        zeroIndex.append(ind)
                randomValues = []
                for i in range(numOfPlaceholders):
                    if i == replaceIndex:
                        randomValues.append(letter)
                    elif i in zeroIndex:
                        randomValues.append('0')
                    else:
                        randomValues.append(generateRandomString(1))
                formatedText = ''.join(randomValues)
                text = ''
                for l in formatedText:
                    text = text + ' ' + l
                print(text)
            cursor.execute("update servers set firewalllvl = (%s) where ip = (%s)", (lvl, serverIp))
            mydb.commit()

        elif lvl == 1:
            lvl -= 1
            for letter in firewallpwd[index]:
                numOfPlaceholders = 20
                replaceIndex = random.randint(0, numOfPlaceholders - 1)
                zeroIndex = []
                while len(zeroIndex) < 15:
                    ind = random.randint(0, numOfPlaceholders - 1)
                    if len(zeroIndex) == 0 and ind != replaceIndex:
                        zeroIndex.append(ind)
                    elif zeroIndex.__contains__(ind) == False and ind != replaceIndex:
                        zeroIndex.append(ind)
                randomValues = []
                for i in range(numOfPlaceholders):
                    if i == replaceIndex:
                        randomValues.append(letter)
                    elif i in zeroIndex:
                        randomValues.append('0')
                    else:
                        randomValues.append(generateRandomString(1))
                formatedText = ''.join(randomValues)
                text = ''
                for l in formatedText:
                    text = text + ' ' + l
                print(text)
            cursor.execute("update servers set firewalllvl = (%s) where ip = (%s)", (lvl, serverIp))
            mydb.commit()

        elif lvl == 0:
            for letter in firewallpwd[index]:
                numOfPlaceholders = 20
                replaceIndex = random.randint(0, numOfPlaceholders - 1)
                zeroIndex = []
                while len(zeroIndex) < 19:
                    ind = random.randint(0, numOfPlaceholders - 1)
                    if len(zeroIndex) == 0 and ind != replaceIndex:
                        zeroIndex.append(ind)
                    elif zeroIndex.__contains__(ind) == False and ind != replaceIndex:
                        zeroIndex.append(ind)
                randomValues = []
                for i in range(numOfPlaceholders):
                    if i == replaceIndex:
                        randomValues.append(letter)
                    elif i in zeroIndex:
                        randomValues.append('0')
                    else:
                        randomValues.append(generateRandomString(1))
                formatedText = ''.join(randomValues)
                text = ''
                for l in formatedText:
                    text = text + ' ' + l
                print(text)


def replace(filename, oldtext, newtext):
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    cursor.execute("select * from files where ip = (%s) and path = (%s)", (serverIp, currentPath))
    file = cursor.fetchall()
    found = False
    for i in file:
        if filename == i[1] + '.' + i[3]:
            found = True
            name = i[1]
            path = i[2]
            extension = i[3]
            content = i[4]
            break
    if found == True:
        if len(content) >= len(oldtext):
            content=content.replace(oldtext, newtext)
        cursor.execute("update files set content = (%s) where ip = (%s) and path = (%s) and name = (%s) and extension = (%s)", (content, serverIp, path, name, extension))
        mydb.commit()


def reboot():
    print("Reboot in: ")
    for i in reversed(range(5)):
        print(i+1)
        sleep(1)
        print("sth should happen")


def cat(filename):
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    cursor.execute("select * from files where ip = (%s) and path = (%s)", (serverIp, currentPath))
    file = cursor.fetchall()
    found = False
    for i in file:
        if filename == i[1] + '.' + i[3]:
            found = True
            content = i[4]
            break
    if found == True:
        start = 0
        stop = 100
        print(filename)
        while start < len(content):
            print(content[start:stop])
            start+=100
            stop+=100
    else:
        print(f"File {filename} not found")


def disconnect():
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    index = 0
    cp = currentPath
    for i in ips:
        if i == serverIp:
            break
        else:
            index+=1
    if serverIp != ips[0]:
        cursor.execute("update servers set firewalllvl = (%s), firewall = (%s), proxy = (%s), ssh = (%s), ftp = (%s), smtp = (%s), http = (%s) where ip = (%s)", (firewalllvl[index], firewalls[index], proxys[index], sshs[index], ftps[index], smtps[index], https[index], serverIp))
        cursor.execute("update servers set connected = False, logged = False where ip = (%s)", (serverIp, ))
        cursor.execute("update servers set connected = True where ip = (%s)", (ips[0], ))
        cursor.execute("update hackedports set hacked = False")
        mydb.commit()
        print(f"Disconnected from {serverIp}")
        cp = ''
    return cp


def exe():
    cursor.execute("select ip from servers where name = 'Players PC'")
    playerIp = cursor.fetchone()[0]
    cursor.execute("select * from files where ip = (%s)", (playerIp, ))
    file = cursor.fetchall()
    for i in file:
        if i[3] == 'exe':
            print(f"{i[1]}.{i[3]}")


def probe():
    cursor.execute("select * from servers where connected = True")
    allinfo = cursor.fetchone()
    securities = [allinfo[2], allinfo[3], allinfo[4], allinfo[5], allinfo[6], allinfo[7], allinfo[8]]
    securitiesStr = []
    for i in securities:
        if i == 1:
            securitiesStr.append("Active")
        elif i == 0:
            securitiesStr.append("Inactive")
    print(f"Open ports required for crack: {securities[0]}\nFirewall: {securitiesStr[5]}\nProxy: {securitiesStr[4]}\nport#: 80 -HTTP Webserver: {securitiesStr[3]}\nport#: 25 -SMTP Mailserver: {securitiesStr[2]}\nport#: 21 -FTP Server: {securitiesStr[1]}\nport#: 22 -SSH: {securitiesStr[0]}")


def connect(targetIp):
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    cursor.execute("select * from nearby where sourceip = (%s) and visible = True", (serverIp, ))
    visibleIps = cursor.fetchall()
    cp = ''
    for i in visibleIps:
        index = 0
        for j in ips:
            if i[1] == j:
                break
            else:
                index+=1
        if targetIp == i[1]:
            cursor.execute("update servers set connected = False where ip = (%s)", (serverIp, ))
            cursor.execute("update servers set connected = True where ip = (%s)", (targetIp, ))
            mydb.commit()
            print(f"Connected to {ips[index]} - {names[index]} server")
            cp = ''
            break
        else:
            cp = currentPath
    return cp


def mv(filename, destination):
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    cursor.execute("select * from folders where ip = (%s)", (serverIp, ))
    folder = cursor.fetchall()
    cursor.execute("select * from files where ip = (%s) and path = (%s)", (serverIp, currentPath))
    file = cursor.fetchall()
    found = False
    success = False
    for i in file:
        if filename == i[1] + '.' + i[3]:
            found = True
            name = i[1]
            extension = i[3]
            content = i[4]
    if found == True:
        for i in folder:
            if (destination == i[1] or destination == i[2] + i[1]) and serverIp == folder[0][0]:
                cursor.execute("insert into files values(%s, %s, %s, %s, %s)", (serverIp, name, destination, extension, content))
                cursor.execute("delete from files where name = (%s) and extension = (%s) and path = (%s) and ip = (%s) and content = (%s)", (name, extension, currentPath, serverIp, content))
                success = True
                mydb.commit()
        if success == True:
            print(f"Moved file {filename} to {destination}")
        else:
            print("Invalid destination")
    else:
        print(f"File {filename} not found")


def cd(directory):
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    cursor.execute("select * from folders where ip = (%s) and path = %s", (serverIp, currentPath))
    folder = cursor.fetchall()
    cp = ''
    if directory == '' or directory == None:
        cp = ''
    elif directory == '..':
        if currentPath != '':
            parts = str(currentPath).split("/")
            l = len(parts)
            if l != 1:
                for i in range(len(parts) - 1):
                    if parts[i] != '':
                        cp = cp + '/' + parts[i]
            else:
                cp = ''
    else:
        cp = currentPath
        for i in folder:
            if directory == i[1]:
                cp = currentPath + directory
                break
            else:
                cp = currentPath
    return cp


def ls():
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    cursor.execute("select * from folders where ip = (%s) and path = (%s)", (serverIp, currentPath))
    folder = cursor.fetchall()
    for i in folder:
        print(i[1])
    cursor.execute("select * from files where ip = (%s) and path = (%s)", (serverIp, currentPath))
    file = cursor.fetchall()
    for i in file:
        print(i[1] + '.' + i[3])


def rm(filename):
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    cursor.execute("select * from files where path = (%s) and ip = (%s)", (currentPath, serverIp))
    file = cursor.fetchall()

    if filename != '*':
        msg = f"File '{filename}' not found"
    else:
        msg = "There were no files to remove"

    for i in range(len(file)):
        if file[i][1] + '.' + file[i][3] == filename:
            cursor.execute("delete from files where name = (%s) and extension = (%s) and ip = (%s)", (file[i][1], file[i][3], serverIp))
            mydb.commit()
            msg = f"Removed file '{filename}'"
            break
        elif filename == '*':
            cursor.execute("delete from files where ip = (%s) and path = (%s)", (serverIp, currentPath))
            mydb.commit()
            msg = f"Removed all files from {currentPath} folder"
            break
        else:
            if filename != '*':
                msg = f"File '{filename}' not found"
            else:
                msg = "There were no files to remove"
    print(msg)


def scan():
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    cursor.execute("select * from nearby where sourceip = (%s) and visible = True", (serverIp,))
    visibleIps = cursor.fetchall()
    for i in visibleIps:
        index = 0
        for j in ips:
            if i[1] == j:
                break
            else:
                index += 1
        print(f"{i[1]} - {names[index]}")


def scp(filename, destination=None):
    cursor.execute("select ip from servers where connected = True")
    serverIp = cursor.fetchone()[0]
    cursor.execute("select * from files where path = (%s) and ip = (%s)", (currentPath, serverIp))
    file = cursor.fetchone()
    if file == None:
        print(f"File {filename} not found")
    else:
        if file[1] + '.' + file[3] == filename:
            name = file[1] + '.' + file[3]
            if destination is not None:
                cursor.execute("select * from folders where ip = (%s)", (ips[0], ))
                playerFolders = cursor.fetchall()
                goodDestination = False
                for i in playerFolders:
                    if i[1] == destination:
                        cursor.execute("insert into files values(%s, %s, %s, %s, %s)", (ips[0], file[1], destination, file[3], file[4]))
                        goodDestination = True
                        mydb.commit()
                        break
                    elif i[2] == destination and destination != "":
                        cursor.execute("insert into files values(%s, %s, %s, %s, %s)", (ips[0], file[1], destination, file[3], file[4]))
                        goodDestination = True
                        mydb.commit()
                        break
                    elif destination == "":
                        break
                if goodDestination == False:
                    print("Incorrect 'destination' value")
            else:
                cursor.execute("insert into files values(%s, %s, %s, %s, %s)", (ips[0], file[1], '/bin', file[3], file[4]))
                mydb.commit()
        else:
            print(f"File '{filename}' not found")


def help():
    for h in range(len(patterns)):
        print(patterns[h] + " - " + definitions[h])


def check_pattern(input_string):  # zostalo chyba tylko to
    # Split the input into separate parts
    parts = input_string.split()

    # Check if the input has the correct number of parts
    if len(parts) >= 4 and parts[0] == "replace":
        placeholder = parts[1].replace("'", "")
        i=2
        value = []
        ind = 0
        opened=False
        for j in range(len(parts)):
            if j >= i:
                if parts[j][0] == "'" and parts[j][len(parts[j])-1] == "'":
                    value.append(parts[j])
                    ind+=1
                elif parts[j][0] == "'":
                    value.append(parts[j])
                    opened = True
                elif opened == True and parts[j][len(parts[j])-1] == "'":
                    value[ind] = value[ind] + " " + parts[j]
                    ind+=1
                    opened = False
                elif opened == True and parts[j][len(parts[j])-1] != "'":
                    value[ind] = value[ind] + " " + parts[j]

        value[0] = value[0].replace("'", "")
        value[1] = value[1].replace("'", "")

        # Check if the input matches the pattern
        #print("replace {} '{}' '{}'".format(placeholder, value[0], value[1]))
        if input_string == "replace {} '{}' '{}'".format(placeholder, value[0], value[1]):
            replace(placeholder, value[0], value[1])
            return True
        else:
            return False

    elif len(parts) == 3:
        index = 0
        for c in range(len(commands)):
            if parts[0] == commands[c] and lengths[c] == 3:
                value1 = parts[1]
                value2 = parts[2]
                if input_string == patterns[c].format(value1, value2):
                    if parts[0] == "scp":
                        scp(value1, value2)
                        return True
                    elif parts[0] == "mv":
                        mv(value1, value2)
                        return True
                    elif parts[0] == "append":
                        append(value1, value2)
                        return True
                    else:
                        return False
            else:
                index += 1
        if index >= len(commands):
            return False

    elif len(parts) == 2:
        index = 0
        for c in range(len(commands)):
            if parts[0] == commands[c] and lengths[c] == 2:
                value1 = parts[1]
                if input_string == patterns[c].format(value1):
                    if parts[0] == "scp":
                        scp(value1)
                        return True
                    elif parts[0] == "rm":
                        rm(value1)
                        return True
                    elif parts[0] == "cd":
                        currentPath = cd(value1)
                        return currentPath
                    elif parts[0] == "connect":
                        currentPath = connect(value1)
                        return currentPath
                    elif parts[0] == "cat":
                        cat(value1)
                        return True
                    elif parts[0] == "solve":
                        solve(value1)
                        return True
                    elif parts[0] == "upload":
                        upload(value1)
                        return True
                    elif parts[0] == "sshcrack":
                        sshcrack(value1)
                        return True
                    elif parts[0] == "ftpbounce":
                        ftpbounce(value1)
                        return True
                    elif parts[0] == "smtpoverflow":
                        smtpoverflow(value1)
                        return True
                    elif parts[0] == "webserverworm":
                        webserverworm(value1)
                        return True
                    elif parts[0] == "porthack":
                        porthack(value1)
                        return True
                    elif parts[0] == "nano":
                        nano(value1)
                        return True
                    elif parts[0] == "mkdir":
                        mkdir(value1)
                        return True
                    elif parts[0] == "rmdir":
                        rmdir(value1)
                        return True
                    else:
                        return False
            else:
                index += 1
        if index >= len(commands):
            return False

    elif len(parts) == 1:
        index = 0
        for c in range(len(commands)):
            if parts[0] == commands[c] and lengths[c] == 1:
                if parts[0] == "help":
                    help()
                    return True
                elif parts[0] == "scan":
                    scan()
                    return True
                elif parts[0] == "ls":
                    ls()
                    return True
                elif parts[0] == "probe":
                    probe()
                    return True
                elif parts[0] == "exe":
                    exe()
                    return True
                elif parts[0] == 'cd':
                    cd('')
                elif parts[0] == "disconnect" or parts[0] == "dc":
                    disconnect()
                    currentPath = ''
                    return currentPath
                elif parts[0] == "reboot":
                    reboot()
                    return True
                elif parts[0] == "analyze":
                    analyze()
                    return True
                elif parts[0] == "login":
                    login()
                    return True
                elif parts[0] == "clear":
                    clear()
                    return True
                elif parts[0] == "shell":
                    shell()
                    return True
                elif parts[0] == "overload":
                    overload()
                    return True
                elif parts[0] == "quit":
                    quit()
                    return True
                else:
                    return False
            else:
                index += 1
        if index >= len(commands):
            return False
    else:
        return False


while True:
    # Get input from the user
    user_input = input(f"{currentPath}{insertIcon} ")
    # Call the function to check the pattern
    if check_pattern(user_input) == True:
        pass
        #print("Input follows the pattern")
    elif check_pattern(user_input) == False:
        print("Incorrect/unknown command. Insert 'help' to see all available commands\n")
        #print("Input does not follow the pattern")
    else:
        if check_pattern(user_input) != None:
            oldl = len(currentPath)
            currentPath = check_pattern(user_input)
            newl = len(currentPath)
            if oldl < newl:
                currentLvl+=1
            elif oldl > newl:
                currentLvl-=1
        else:
            currentPath = ''
            currentLvl = 0  # dodaj to do funkcji

""

"""
# Create and start the timer thread
timer_thread = threading.Thread(target=countdown_timer, args=(10,))
timer_thread.start()

# Perform actions in the main thread
do_something()

# Wait for the timer thread to complete
timer_thread.join()
"""

"""for i in range(32):
    cursor.execute("insert into servers values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (ips[i], names[i], oprfcs[i], sshs[i], ftps[i], smtps[i], https[i], proxys[i], firewalls[i], logins[i], passwords[i], pwdaquired[i], False))
mydb.commit()
"""
"""
for i in range(32):
    cursor.execute("insert into folders values(%s, %s, %s)", (ips[i], '/home', ''))
    cursor.execute("insert into folders values(%s, %s, %s)", (ips[i], '/bin', ''))
    cursor.execute("insert into folders values(%s, %s, %s)", (ips[i], '/log', ''))
    cursor.execute("insert into folders values(%s, %s, %s)", (ips[i], '/sys', ''))
mydb.commit()
"""
"""for s in range(len(serverIndex)):
    cursor.execute("insert into nearby values(%s, %s, %s)", (ips[serverIndex[s]], ips[secondServerIndex[s]], False))
    mydb.commit()
for s in range(len(rest)):
    cursor.execute("insert into nearby values(%s, %s, %s)", (ips[0], ips[rest[s]], False))
    mydb.commit()"""
"""for s in range(len(ips)):
    cursor.execute("insert into shells values(%s, %s)", (ips[s], False))
    mydb.commit()"""

