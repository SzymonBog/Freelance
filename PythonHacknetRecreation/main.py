import os
import sqlite3
from random import randint, choice
from string import ascii_letters
import time  # for emails
import math  # -
import threading  # -
# from mysql import connector # -
from time import sleep  # -
import pygame as pg

# In some places I have this warning: 'Local variable might be referenced before assignment'
# but I made sure that it won't happen(using commands 'if', 'try' and  'return' :D)

# For now, I don't care about PEP-8(I'll try and do it later) because my first priory is make it work and then make it look(and I have a bit less scrolling XD)

# Ctrl + R  - refactor
# Ctrl + /  - comment
# add check if logged(certain actions require being logged in)!!!!
# MySQL - changed in code(added some variables)
"""
servers: IP varchar, name varchar, ssh #22 boolean, ftp server #21 boolean, smtp mailserver #25 boolean, http webserver #80 boolean, required port number for crack int, connected boolean
# ssh, ftp, smtp, http: only stores info if it was hacked(always implemented: default - true)
connections: sourceIP varchar, connectionIP1 varchar, connectionIP2 varchar
directories: IP varchar, path varchar, directoryName varchar \/
files: name varchar, extension varchar, content varchar, directory foreign key \/
emails: sender varchar, receiver varchar, content varchar, attachment foreign key(files) \/
"""
# UNIX - '\/'-done, '/'-rejected(I'm not doing it, there is no sense)
"""
help - lists all commands \/
scp {filename} - copy file to '/bin' \/
scp {filename} {destination} - copy file to destination \/
scan - scans for links on the connected machine \/
rm {filename (or *)} - delete specified file(all files) \/
ps - lists currently running processes and their PIDs /
kill {PID} - kills process number PID /
cd {foldername} - moves current working directory to the specified folder \/
mv {file} {destination} - moves or renames {file} to {destination} (mv hi.txt ../bin/hi.txt)  # you can base on scp \/
connect {ip} - connect to external computer \/
probe - scans the connected machine for active ports and security level \/
exe - lists all available executables in the local /bin/ folder \/
disconnect - terminate the current open connection \/
dc - terminate the current open connection \/
cat {filename} - displays contents of file \/
reboot - reboots the connected computer / - for now I see no sense
replace {filename} {text to replace} {replacement} - replaces the target text in the file with the replacement \/
analyze  - rerforms an analysis pass on the firewall of the target machine(Note: the command must be used a at least 6 times to reveal the clear firewall solution.)  height=6, width=20 \/
solve {firewall solution} - attempts to solve the firewall of the target machine to allow UDP Traffic \/
login {username} {password} - requests a username and password to log in to the connected system \/
upload {local file path/filename} - uploads the indicated file on your local machine to the current directory \/
clear - clears the terminal / - it would make things more complicated
append {filename} {data} - appends a line containing {data} to file {filename}(Note: appending uses a new line every time the command is used.) \/
shell - opens a remote access shell on target machine with Proxy overload and IP trap capabilities \/
overload - overloads proxy server(requires at least 1 shell, the more shells you have the faster it will overload[28/n]) \/ seems ok
sshcrack 22 - unlock port 22 using 'SSHCrack.exe'  \/
ftpbounce 21 - unlock port 21 using 'FTPBounce.exe'  \/
smtpoverflow 25 - unlock port 25 using 'SMTPoverflow.exe'  \/
webserverworm 80 - unlock port 80 using 'WebServerWorm.exe'  \/
porthack {port number} - hack port if player unlocked required number of ports to crack \/
resetDB  - resets all data in database(loose all progress)[CAREFUL!!!!!!!] \/
quit - exits the program \/
"""
# Logs
"""
scp - @1579_FileDownloaded:_by_70.183.159.171_-_file:filename.ext  \/
rm - @1546_FileRemoved:_by_70.183.159.171_-_file:filename.ext  \/
mv - @1530_FileMoved:_by_70.183.159.171_-_file:filename.ext  \/
connect - @1467_Connection:_from_70.183.159.171  \/
disconnect - @1496_70.183.159.171_Disconnected  \/
cat - @1534_FileRead:_by_70.183.159.171_-_file:filename.ext  \/
replace - @1543_FileChanged:_by_70.183.159.171_-_file:filename.ext  \/
login - @1496_70.183.159.171_Became_Admin  \/
upload - @1564_FileUploaded:_by_70.183.159.171_-_file:filename.ext  \/
append - @1552_FileAppended:_by_70.183.159.171_-_file:filename.ext \/
nano - @1566_FileCreated:_by_70.183.159.171_-_file:filename.ext  \/
       @1568_FileModified:_by_70.183.159.171_-_file:filename.ext \/
"""

# 24+2/29 (32-all; 29-accepted; 3-rejected) +1
# this code will probably have sth about 2100 lines(but I think it will be more)
# And yeah, I have too much free time
# arrows(up, down) work :)

# remember to turn on apache and mysql in xampp
# mydb = connector.connect(
#    host='127.0.0.1',
#    user='admin',
#    password='123456',
#    port=3306,
#    database='hacknetrecreation'
# )

mydb = sqlite3.connect('hacknetrecreation.db')  # sqlite3


def createTables(cursor: mydb.cursor(), mydb) -> None:  # not finished{almost :), well not almost XD }
    # ---------------------------------------------
    # Only for players PC
    # directories variables <- ip from servers vars
    directoryPathsPlayer = ["", "", "", "", "home", "home"]
    directoryNamesPlayer = ["home", "log", "bin", "sys", "stash", "misc"]

    # files variables <- ip from servers vars
    filePathsPlayer = ["bin", "sys", "sys", "sys", "sys"]
    fileNamesPlayer = ["SecurityTracer", "x-server", "os-config", "bootcfg", "netcfgx"]
    fileExtensionsPlayer= ["exe", "sys", "sys", "dll", "dll"]
    fileContentsPlayer = ["110101010111111100101101110111001100110011011100111111100110010111\n001010111100000000000010011101011101101010111101001011101001110110\n110000101010010100111001011111010001001110111011110101010110100111\n010011010001011010001010011001101100110000010100111000010010100111\n010011001100000001111001110110000111011010001001010011011000110111\n000110110010110110111110111111001010111001000100100110101101100000\n100111000010001000011011001110110010101110011110011011000000000100\n10101101110111110011001111100101100111111001001001", "7297991071101011166610811710149", "100100000001000101000010110000001010001001100101110101001111101100\n011000010010110101110011000110101110101110110100110010011100110111\n111110100110011101010000000011001000001110100101100011100101110100\n100011100100111111111010001011111101001000101000111100101100010000\n011011111001110011011100011100011001100011000100001110000100011000\n000100011111000100101011000000010011011100001100101101000011100011\n111101000101011111100010100110011000011101000111001110111111110110\n011100100010101110101111110000000110000101010101101011011110111100\n010101011101010110100010011", "110000111000010010010011101000100001011101010101010101110010010111\n010010100100101010100010111111010101011000011001110011110001011101\n111000010111101111101010101011001001000011011111010001000111010011\n000111000000000100111101110001000101000100110001011110010010101101\n110011100010010011011010100000001011010101110001111010011001111010\n111010110000100001010110010100100110010001010111100000011010111111\n110010110010011100000101101111111010001101011111001011110010101011\n0000111110011100011101110001001111010111000110000111111110110", "101110000001100001100000011100111000000011111110001011100100111111\n111011011101100111101110101101101011010010000111011100110001100100\n000001000000110000011000011100000100011000001001010100000101110001\n000001100100000110001001011111100000000011101011111110001001100100\n010000111110100001111101110001100110011111101010111101101010011000\n101101010110110100000010001011000011100011100000000001111011101010\n001100110001100000000110000000000001000100011101110101000110111011\n10101100011001100001111011110011010000011011"]
    # ---------------------------------------------
    # Only for Photonic Studios
    # directories variables <- ip from servers vars
    directoryPathsPhotonicStudios = ["", "", "", "", "home", "home", "home", "home"]
    directoryNamesPhotonicStudios = ["home", "log", "bin", "sys", "Newfolder5", "Newfolder70", "Newfolder81", "Newfolder80"]

    # files variables <- ip from servers vars
    filePathsPhotonicStudios = ["sys", "sys", "sys", "sys", "home/Newfolder80", "home/Newfolder80", "home/Newfolder81", "home/Newfolder81", "home/Newfolder70", "home/Newfolder5", "home/Newfolder5", "bin"]
    fileNamesPhotonicStudios = ["netcfgx", "bootcfg", "os-config", "x-server", "IRC_Log:9322+(12328)", "IRC_Log:258908+(15060)", "IRC_Log:412248+(11135)", "Data18", "IRC_Log:4281+(27825)", "Data229", "Data89", "config"]
    fileExtensionsPhotonicStudios = ["dll", "dll", "sys", "sys", "", "", "", "", "", "", "", "txt"]
    fileContentsPhotonicStudios = ["1101010111110010110001100111100011010100100100000111101101111110\n0010111000000001000011011110110011100001101011000110100000011011\n1000111011110001111110101100111000001110011001110001100111000111\n0111101111001000000111111100111001111010000110100011101001110110\n1110010111101001011001001000111000011111111010010110010101000111\n1000100101101110110100100110110001011111100000010011100101001111\n1110000001000101100111111101010101000011001000010011110011101000\n0111000101111010111011001000000010010001100100000000001010101111\n1000010100010011000100011000000101010111111000110000000110101001\n0101100010001010010000101111001001011010011101111010001110001", "1010101110011101011011011001101111101001110010101011100011111110\n1101000011101110110010111111100011010000010011111011001100000110\n0110101010100011100011111000000000101000100100101101000110000000\n1011000111101000000001100111011000010001101110110011101000110101\n0110001010101000100000001001011111101110101011110110100011110101\n0010011010101110010101111010110111110100000100110010101101010000\n1110101000000000100100000111011110011000111101111100011011100000\n1110110101000110100111110100110011000000000011100100101000011110\n0010100110100110000100110011110110100111111111010110111100101010\n100010100010", "1000111010100001101111111111111000011101011010100001100111110100\n0010111101111000110001000010100010110001100010101001011001100011\n1111000011001011011111110110101011001001111111100110010001110001\n0001000111001101111010011011000000101101101010001010000010110101\n1000000010000110000110110000111111010100101010001001011111010111\n0110100111101010011001101000001111000001101100101010110100001000\n0010100000001111111111100110011100000101011111000010001111011010\n1111001010011001000101000100110111111011101010111111110100000110\n0101011000011000010101110000000010101010010101110000000010111001\n010001111010101011111010100000011000000", "7297991071011147111410110111052", "<tag> Ouroboros: lets play Pong\n<Ouroboros> Ok.\n<tag> |  .\n<Ouroboros>.  |\n<tag> | .\n<Ouroboros>  .|\n<tag> |.\n<Ouroboros>   |.\n<Ouroboros> Whoops\n\nArchived Via : http://Bash.org", "<Ben174> : If they only realised 90% of the overtime they pay me is only cause i like\nstaying here playing with Kazaa when the bandwidth picks up after hours.\n\n<ChrisLMB> : If any of my employees did that they'd be fired instantly.\n<Ben174> Where u work?\n<ChrisLMB> : I'm the CTO at LowerMyBills.com\n*** Ben174 (BenWright@TeraPro33-41.LowerMyBills.com) Quit (Leaving)\n\nArchived Via : http://Bash.org", "<Locl-Yocl> I helped the EMTs at a car wreck and got blood all over my arms and shirt. It\nlooked like I murdered 20 people with a fork... anyway, I walked into a convieniance \nstore down the street and said my girlfriend needs a tampon. The guy at the counter was\nmortified.\n\nArchived Via : http://Bash.org", "1101110101110101111110000010111001000010100011100111111010101110\n1000100011100100110111101110000100001100000011111001111111010011\n1010000100000110010010110101111001110101100000111000100110011110\n1100110101111110100011110011100011000000001000111010011101100011\n1001001001100101000101011011101010011101111000000100001110110010\n1000001011101101001000011111010111100110110011010110101001000010\n0100101100010010010000000000111010101011001110100101011001110010\n1111000010111010000110101010010111000010000", "<Zybl0re> get up\n<Zybl0re> get on up\n<Zybl0re> get up\n<Zybl0re>get on up\n<phxl|paper> and DANCE\n* nmp3bot dances :D-<\n* nmp3bot dances :D|-<\n* nmp3bot dances :D/-<\n<[SA]HatfulOfHollow> i'm going to become rich and famous after i invent a device that\nallows you to stab people in the face over the internet\n\nArchived Via : http://Bash.org", "000110000101111100110010100011001101110010111111010001010001100111100000001100110001010001110111101011011111000000011000010011100100101110010010000101111100000110111000101111001001001011110110111100110011001101010001000011111001000011010000011101010111010100110100000011010001100001100100001001000010001111010110110110100001001110101000100101100110000010110100001000011011010000101000010111", "001011110011100000001010001011101101101001110001000000101101101010111101110111011110010101000110101111001110110011100101000010011000010111010000001011000000000001110100011101011001011100110100111100101100110100110110110011111001010100010110111100000101110101100100111101100011111010010110111101100001011101000110011100001111010101000000001001101011100010100011110011000010001111010101010100000011111100010011011011000111", "config.ini\ninit_num: '12'\ncontinual_spawning 'YES'\ncolours_enabled {'peach', 'ivory', 'fudge', 'chocolate', 'magenta'}\nbehaviours_enabled {'twirl', 'thrust', 'helicopter'}\nresolution: {'1280', '800'}\nfullscreen: 'YES'\nalt_tab_enabled: 'YES'\ntexture_folder:\n'C:/Documents_and_Settings/Admin/Fax/Hot_Porn/Documents/Serious_Documents/System/\ntextures'"]
    # ---------------------------------------------
    # Only for Viper-Battlestation
    # directories variables <- ip from servers vars
    directoryPathsViperBattlestation = ["", "", "", "", "home"]
    directoryNamesViperBattlestation = ["home", "log", "bin", "sys", "work"]

    # files variables <- ip from servers vars
    filePathsViperBattlestation = ["sys", "sys", "sys", "sys", "bin", "home", "home", "home", "home", "home/work", "home/work", "home/work", "home/work"]
    fileNamesViperBattlestation = ["x-server", "os-config", "bootcfg", "netcfg", "SSHcrack", "EmailDraft", "asdf", "Notes", "Youtubers", "seb", "ripped_prerelease", "TARGET", "jasperlog"]  # SSHcrack: position - 5, index - 4
    fileExtensionsViperBattlestation = ["sys", "sys", "dll", "dll", "exe", "txt", "txt", "txt", "txt", "txt", "log", "txt", "txt"]
    fileContentsViperBattlestation = ["729799107110101116841019710850", "001111011101000100100011010001111100101001010011001001011111111001101000100\n000100110000000110001010111011110111000111011110110001110101010101010010011\n100010010011000100001001011011010000101001000001011011100011000110011110000\n100010110111111100101000010001010111101111000111000100111000110000001011001\n101111011001100101010110110010011100010010011111111011010011001000001010", "011010001011100010010111101100100111100101001010000010110001010110001001100\n001100111001111011000101100010111110000001010011010010001100110111000111010\n101111010111001111001111000001001110101101110100001010110100101011011100101\n100111111010100100101111000001001011001110000101101010101100000011110100011\n110111010111111111111110101001101100010110101100010110000100001101100111001\n100100000001011011110010000101111010001011111", "001001001011011000111000111100110001100011010101001100101100000011011010101\n001001111010010010110111000010100001101101111111110101010010111010000010010\n110000110100101111111000100100101000101010101011000010101010010100110110001\n010011010001011000101110001110000101010101110100000110001011100111100111101\n111001001011000010101101101011010011001011111110110110011001110001100", "110111000110111010001000001111000111110001000001100110110011100010100110101\n011111010010011100011101010100111010110110111100111000101001100010010010111\n110000010000010110100001110101100000110110011010001100010111010101101010111\n110110010111110111001111110011001010111010000111010001001001111100100100110\n100110101101101010110111110111111010000000001001110111001111111101010110000\n11011110110001111111010101110", "Dad,\nSorry I haven't emailed you in a while - I've been really busy with school - year 11 is \nhard, but I think I'm doing ok.\n\nI actually wanted to ask for a little help - I need some new software for a school \nproject. It's called 'FTPBounce.exe'. It's really useful! It'll cost a lot though, and I've \nrun out of the money you sent me last time - all this IT project software is really \nexpensive.\n\nIs there any chance you could send another $2,000 to my account? It'd really help out.\n\nThanks!\nLove you,\nTim", "Induction test?\n199.59.149.230\nProxy server\n\n..\n\nNeed something about overloading it maybe?\nGot to research it more. Maybe there's a program to help? Will ask for more money..", "Finally managed to torrent that sweet new haxxor program from the server Gollum told \nme about - this is so sick!\n\nCant wait to try it out - just got to work out hot to use it first", "youtubers to check out:\n\ncaptainspinifex\nrockleesmile\nnorthernlion\nofficalcalemgames\njonathancrowgamer", "[viper] How did it go?\n[lilsebastian] It was a nightmare.\n[viper] Why?\n[lilsebastian] We spent the night at the lookout. It was super romantic.\n[lilsebastian] Then we started making out.\n[lilsebastian] Then started fooling around, you know.\n[lilsebastian] And then, er.\n[viper] What?\n[viper] Spit it out.\n[lilsebastian] It err, ended sooner than expected. Like. Clothes still on sooner.\n[viper] ......\n[viper] ......\n[viper] HAHAHAHAHAHHAHAHAHAHAHHAA\n[lilsebastian] Shut up.\n[viper] Dude, god dude, never admit that to anyone again.\n[viper] You're lucky we'er friends, otherwise I'd tell everyone that story.\n[viper] Anyway, gotta go. Got more coding to do.\n[lilsebastian] All good. See you at school tomorrow.\n[viper] Don't get there too early.", "[glaylor] YOU FUCKED IT UP\n[glaylor] 18 MONTHS DEV TIME\n[glaylor] 3 MILLION DOLLARS\n[glaylor] FOR A GAME ABOUT WATCHING MOBILE PHONE SCREENS\n[glaylor] ..........\n[hoops] Whoa, calm down man, people are going to love this\n[hoops] It's like, a statement, on the state of the word.\n[hoops] Like, have you ever walked down the street lately?\n[hoops] People always have their heads buried in their phones, they don't even notice \nit.\n\n[hoops] So we made a game that has you driving, walking, shooting, and hacking, while \nconstantly looking at their phones.\n\n[hoops] It's genius.\n[glaylor] The board is going to have my ass for this.\n[glaylor] We better give it a good name.\n[glaylor] And some hardcore box art.\n[glaylor] And add some bloom effects. That always gets the kids.", "[viper] I want a refund.\n[cs#1575] I'm sorry sir, but we cannot refund based on change of mind.\n[cs#1575] Might I suggest you that you re-list the item on J-Bay?\n[viper] I don't want to list the item on your damn auction site.\n[viper] I told you, I accidentally hit the bid button instead of the watch button\n[cs#1575] I am sorry sir, but our policy doesn't cover accidental button presses.\n[cs#1575] So you will have to accept that the Penetrator 9000 is yours, or you can try \nto recouperate the costs via out acution listings.\n\n[viper] You have messed with the wrong customer. I will make you rue this day.\n[cs#1575] Thank you sir, and may I wish you have a pleasant evening.", "[viper] you got those keys I asked for?\n[jasper] you got the cash?\n[viper] got it ready to be wired\n[jasper] I have uploaded the first half on the drop server. Once the transfer has been \ncompleted you will get the final keys.\n\n[viper] cool. checking it out now.\n[viper] awesome. they work.\n[jasper] can I have my money now?\n[viper] sent\n[jasper] recieved. who would have thought call of soldier would be so popular this year.\n[viper] hottest thing this year.\n[jasper] gamers."]
    # ---------------------------------------------

    # ---------------------------------------------
    # All arrays for loop
    directoryPaths = [directoryPathsPlayer, directoryPathsPhotonicStudios, directoryPathsViperBattlestation]
    directoryNames = [directoryNamesPlayer, directoryNamesPhotonicStudios, directoryNamesViperBattlestation]

    filePaths = [filePathsPlayer, filePathsPhotonicStudios, filePathsViperBattlestation]
    fileNames = [fileNamesPlayer, fileNamesPhotonicStudios, fileNamesViperBattlestation]
    fileExtensions = [fileExtensionsPlayer, fileExtensionsPhotonicStudios, fileExtensionsViperBattlestation]
    fileContents = [fileContentsPlayer, fileContentsPhotonicStudios, fileContentsViperBattlestation]
    # ---------------------------------------------

    # emails variables
    senders = []
    recievers = []
    contents = []
    attachmentNames = []
    attachmentExtensions = []
    attachmentContents = []
    isMailVisible = []

    # servers variables
    ips = ["70.183.159.171", "192.197.182.170", "219.240.94.206"]
    names = ["Your PC", "Photonic Studios", "Viper-Battlestation"]
    logins = ["user", "admin", "admin"]
    passwords = ["password", "doggie", "player"]
    rpfcs = [4, 0, 0]  # required ports to crack
    proxies = [True, False, False]
    firewalls = [True, False, False]
    proxyRequirements = [25, 0, 0]  # number of shells needed to break proxy
    isconnected = [True, False, False]
    isvisible = [True, False, False]
    firewallPasswords = ["gyv67k", None, None]

    # connections variables <- takes sourceIp from server vars
    sources = [ips[0], ips[0]]
    connectionIp = [ips[1], ips[2]]
    # usedCommands <- added in runtime

    # mysql create tables
    cursor.execute("create table directories(ip varchar(15), path varchar(255), name varchar(255))")
    mydb.commit()
    cursor.execute("create table files(ip varchar(15), path varchar(255), name varchar(255), extension varchar(255), content varchar(5000))")
    mydb.commit()
    # for emails add a column with time
    cursor.execute("create table emails(sender varchar(255), reciever varchar(255), content varchar(5000), attachmentName varchar(255), attachmentExtension varchar(255), attachmentContent varchar(2000), visible bit)")
    mydb.commit()
    cursor.execute("create table servers(ip varchar(15) primary key, name varchar(255), ssh bit, ftp bit, smtp bit, http bit, port22 bit, port21 bit, port25 bit, port80 bit, rpfc int, proxy bit, firewall bit, proxyRequirements int, shell bit, connected bit, visible bit, login varchar(255), password varchar(255), logged bit, firewallPassword varchar(6), hasFirewall bit, hasProxy bit)") # add firewall password
    mydb.commit()
    cursor.execute("create table connections(sourceIp varchar(15), connectionIp varchar(15))")
    mydb.commit()
    cursor.execute("create table usedCommands(command varchar(255), printout varchar(6000), linesCount int, currentCommandPath varchar(1000))")
    mydb.commit()

    # mysql insert values
    for i in range(len(ips)):  # change
        for j in range(len(directoryNames[i])):
            cursor.execute("insert into directories values (?, ?, ?)", (ips[i], directoryPaths[i][j], directoryNames[i][j]))
        for j in range(len(fileNames[i])):
            cursor.execute("insert into files values (?, ?, ?, ?, ?)", (ips[i], filePaths[i][j], fileNames[i][j], fileExtensions[i][j], fileContents[i][j]))
        # finish later
        # cursor.execute("insert into emails values ()")
        #
        # \/ should be ok
        cursor.execute("insert into servers values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (ips[i], names[i], True, True, True, True, True, True, True, True, rpfcs[i], proxies[i], firewalls[i], proxyRequirements[i], False, isconnected[i], isvisible[i], logins[i], passwords[i], False, firewallPasswords[i], firewalls[i], proxies[i]))
    for i in range(len(sources)):
        cursor.execute("insert into connections values (?, ?)", (sources[i], connectionIp[i]))
    mydb.commit()


cursor = mydb.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")  # sqlite3
tables = cursor.fetchall()

if len(tables) == 0:
    print("create all tables and insert default values")  #
    createTables(cursor, mydb)

# mydb.commit()


# command definitions
def help(pageNumber) -> (str, int):  # 14, 29: 14:14:1 write it in reverse order
    try:
        pageNumber = int(pageNumber)
        if pageNumber == 1:
            txt = "help {pageNumber} - lists all commands\nscp {filename} - copy file to '/bin'\n" \
              "scp {filename} {destination} - copy file to destination\nscan - scans for links on the connected machine\n" \
              "rm {filename (or *)} - delete specified file(all files)\n" \
              "cd {foldername} - moves current working directory to the specified folder\n" \
              "mv {file} {destination} - moves or renames {file} to {destination} (mv hi.txt ../bin/hi.txt)\n" \
              "connect {ip} - connect to external computer\n" \
              "probe - scans the connected machine for active ports and security level\n" \
              "exe - lists all available executables in the local /bin/ folder\n" \
              "disconnect - terminate the current open connection\ndc - terminate the current open connection\n" \
              "cat {filename} - displays contents of file\nreboot - reboots the connected computer\n"
            number = 14
        elif pageNumber == 2:
            txt = "replace {filename} {text to replace} {replacement} - replaces the target text in the file with the " \
              "replacement\nanalyze  - rerforms an analysis pass on the firewall of the target machine(Note: the command " \
              "must be used a at least 6 times to reveal the clear firewall solution.)\nsolve {firewall solution} - " \
              "attempts to solve the firewall of the target machine to allow UDP Traffic\nlogin {username} {password} - requests a username and" \
              " password to log in to the connected system\nupload {local file path/filename} - uploads the indicated " \
              "file on your local machine to the current directory\nclear - clears the terminal\nappend {filename} {data}" \
              " - appends a line containing {data} to file {filename}(Note: appending uses a new line every time the " \
              "command is used.)\nshell - opens a remote access shell on target machine with Proxy overload and IP trap " \
              "capabilities\noverload - overloads proxy server(requires at least 1 shell\nsshcrack 22 - unlock port 22 " \
              "using 'SSHCrack.exe'\nftpbounce 21 - unlock port 21 using 'FTPBounce.exe'\nsmtpoverflow 25 - unlock " \
              "port 25 using 'SMTPoverflow.exe'\nwebserverworm 80 - unlock port 80 using 'WebServerWorm.exe'\n" \
              "porthack {port number} - hack port if player unlocked required number of ports to crack\n"
            number = 14
        elif pageNumber == 3:
            txt = "quit - exits the program\nresetDB - resets all data in database(loose all progress)[CAREFUL!!!!!!!]\n" \
                  "ls - lists all files and directories in current directory\ntree - shows file and directory structure in a tree\n" \
                  "nano {filename} - create an empty file and write in it or modify existing file"
            number = 5
        else:
            txt = "Page number should be in range 1-3"
            number = 1
    except ValueError:
        txt = "Page number has to be an int"
        number = 1
    return txt, number+1  # it has to be here to make display without visual errors(overlapping)


def scp(currentIp, currentPath, fileName, destination=None) -> (str, int):  # add name changing
    #nameParts = str(txt2).split("/")
    #newName = nameParts[len(nameParts) - 1]

    parts = fileName.split(".")
    if destination is None:
        if len(parts) == 2:
            name = parts[0]
            extension = parts[1]
            cursor.execute("select * from files where ip=? and name=? and extension=? and path=?", (currentIp, name, extension, currentPath))
            file = cursor.fetchone()
            if file is not None:
                content = file[4]
                cursor.execute("insert into files values (?, ?, ?, ?, ?)", ('70.183.159.171', 'bin', name, extension, content))
                mydb.commit()

                log = f'@1579_FileDownloaded:_by_70.183.159.171_-_file:{name}.{extension}'
                cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
                mydb.commit()

                return f"File {fileName} has been successfuly copied to '/bin' folder", 2
            else:
                return "File not found", 2
        elif len(parts) == 1:
            name = parts[0]
            cursor.execute("select * from files where ip=? and name=? and extension=? and path=?", (currentIp, name, '', currentPath))
            file = cursor.fetchone()
            if file is not None:
                content = file[4]
                cursor.execute("insert into files values (?, ?, ?, ?, ?)", ('70.183.159.171', 'bin', name, '', content))
                mydb.commit()

                log = f'@1579_FileDownloaded:_by_70.183.159.171_-_file:{name}'
                cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
                mydb.commit()

                return f"File {fileName} has been successfuly copied to '/bin' folder", 2
            else:
                return "File not found", 2
        else:
            return "Incorrect file name", 2
    else:
        cursor.execute("select * from directories where ip=? and path=?", ('70.183.159.171', destination))
        destin = cursor.fetchall()
        if len(destin) != 0:
            if len(parts) == 2:
                name = parts[0]
                extension = parts[1]
                cursor.execute("select * from files where ip=? and name=? and extension=? and path=?", (currentIp, name, extension, currentPath))
                file = cursor.fetchone()
                if file is not None:
                    content = file[4]
                    cursor.execute("insert into files values (?, ?, ?, ?, ?)", ('70.183.159.171', destination, name, extension, content))
                    mydb.commit()

                    log = f'@1579_FileDownloaded:_by_70.183.159.171_-_file:{name}.{extension}'
                    cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
                    mydb.commit()

                    return f"File {fileName} has been successfuly copied to '/{destination}' folder", 2
                else:
                    return "File not found", 2
            elif len(parts) == 1:
                name = parts[0]
                cursor.execute("select * from files where ip=? and name=? and extension=? and path=?", (currentIp, name, '', currentPath))
                file = cursor.fetchone()
                if file is not None:
                    content = file[4]
                    cursor.execute("insert into files values (?, ?, ?, ?, ?)", ('70.183.159.171', destination, name, '', content))
                    mydb.commit()

                    log = f'@1579_FileDownloaded:_by_70.183.159.171_-_file:{name}'
                    cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
                    mydb.commit()

                    return f"File {fileName} has been successfuly copied to '/{destination}' folder", 2
                else:
                    return "File not found", 2
            else:
                return "Incorrect file name", 2
        else:
            return "Incorrect destination", 2


def scp2(currentIp, currentPath, fileName, destination) -> (str, int):
    cursor.execute("select * from directories where ip=? and path=?", ('70.183.159.171', destination))
    destin = cursor.fetchall()
    parts = fileName.split(".")
    if len(destin) != 0:
        if len(parts) == 2:
            name = parts[0]
            extension = parts[1]
            cursor.execute("select * from files where ip=? and name=? and extension=? and path=?", (currentIp, name, extension, currentPath))
            file = cursor.fetchone()
            if file is not None:
                content = file[4]
                cursor.execute("insert into files values (?, ?, ?, ?, ?)", ('70.183.159.171', destination, name, extension, content))
                mydb.commit()

                log = f'@1579_FileDownloaded:_by_70.183.159.171_-_file:{name}.{extension}'
                cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
                mydb.commit()

                return f"File {fileName} has been successfuly copied to '/{destination}' folder", 2
            else:
                return "File not found", 2
        elif len(parts) == 1:
            name = parts[0]
            cursor.execute("select * from files where ip=? and name=? and extension=? and path=?", (currentIp, name, '', currentPath))
            file = cursor.fetchone()
            if file is not None:
                content = file[4]
                cursor.execute("insert into files values (?, ?, ?, ?, ?)", ('70.183.159.171', destination, name, '', content))
                mydb.commit()

                log = f'@1579_FileDownloaded:_by_70.183.159.171_-_file:{name}'
                cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
                mydb.commit()

                return f"File {fileName} has been successfuly copied to '/{destination}' folder", 2
            else:
                return "File not found", 2
        else:
            return "Incorrect file name", 2
    else:
        destParts = str(destination).split("/")
        cp = ""
        index = 1
        for dp in destParts:
            if index != len(destParts):
                cursor.execute("select * from directories where name=? and ip=? and path=?", (dp, currentIp, cp))
                dest = cursor.fetchone()
                print(dest)
                if dest == None:
                    cursor.execute("insert into directories values (?, ?, ?)", ('70.183.159.171', cp, dp))
                    mydb.commit()
                #else:
                if index == 1:
                    cp += dp
                else:
                    cp += f"/{dp}"
                #    quit(666)
                index += 1
            else:
                dpParts = str(dp).split(".")
                name = dpParts[0]
                ext = ''
                if len(dpParts) > 1:
                    ext = dpParts[1]
                fileNameParts = fileName.split(".")
                cursor.execute("select * from files where ip=? and name=? and extension=? and path=?", (currentIp, fileNameParts[0], fileNameParts[1], currentPath))
                file = cursor.fetchone()
                print(file)
                cont = file[4]
                print(cp)
                cursor.execute("insert into files values (?, ?, ?, ?, ?)", ('70.183.159.171', cp, name, ext, cont))
                mydb.commit()

                log = f'@1579_FileDownloaded:_by_70.183.159.171_-_file:{name}.{ext}'
                cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
                mydb.commit()

                return f"File {fileName} has been successfuly copied to '/{cp}' folder", 2
                #print(dp)
        #print(destParts)
        #quit(0)
        #return "Incorrect destination", 2


def scan(currentIp) -> (str, int):  # modified(use loop(for))
    cursor.execute("select connectionIp from connections where sourceIp=?", (currentIp, ))
    text = cursor.fetchall()
    print(text)
    num = 0
    txt = ""
    #quit(1)
    #text = str(text[0]).replace("('", "").replace("'", "").replace(")", "").split(", ")

    for i in range(len(text)):
        if text[i][0] != "None":

            cursor.execute("select name from servers where ip=?", (text[i][0], ))
            serverName = cursor.fetchone()

            if num != 0:
                txt = txt + "\n" + text[i][0] + " - " + serverName[0]
            else:
                txt += text[i][0] + " - " + serverName[0]
            num += 1
        else:
            txt = "No devices found"
            num = 1
    return txt, num+1


def rm(currentIp, currentPath, fileName, mv=False) -> (str, int):
    parts = fileName.split(".")

    if fileName == "*":
        cursor.execute("delete from files where ip=? and path=?", (currentIp, currentPath))
        mydb.commit()

        if currentPath != 'log':
            if mv == False:
                log = f'@1546_FilesRemoved:_by_70.183.159.171'
                cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
                mydb.commit()  # ?
            else:
                log = f'@1530_FilesMoved:_by_70.183.159.171'  # @1530_FileMoved:_by_70.183.159.171_-_file:filename.ext
                cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
                mydb.commit()

        return "Files have been successfuly deleted", 2
    else:
        cursor.execute("select * from files where ip=? and path=?", (currentIp, currentPath))
        allFiles = cursor.fetchall()
        if len(parts) == 2:
            name, extension = parts[0], parts[1]
        elif len(parts) == 1:
            name = parts[0]
        else:
            return "Incorrect file name", 2
        for f in allFiles:
            if len(parts) == 2:
                if f[2] == name and f[3] == extension:
                    cursor.execute("delete from files where ip=? and name=? and extension=? and path=?", (currentIp, name, extension, currentPath))
                    mydb.commit()

                    if mv == False:
                        log = f'@1546_FileRemoved:_by_70.183.159.171_-_file:{name}.{extension}'
                        cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
                        mydb.commit()
                    else:
                        log = f'@1530_FileMoved:_by_70.183.159.171_-_file:{name}.{extension}'
                        cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
                        mydb.commit()

                    return f"File '{fileName}' has been succesfuly deleted", 2
            elif len(parts) == 1:
                if f[2] == name:
                    cursor.execute("delete from files where ip=? and name=? and path=?", (currentIp, name, currentPath))
                    mydb.commit()

                    if mv == False:
                        log = f'@1546_FileRemoved:_by_70.183.159.171_-_file:{name}'
                        cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
                        mydb.commit()
                    else:
                        log = f'@1530_FileMoved:_by_70.183.159.171_-_file:{name}'
                        cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
                        mydb.commit()

                    return f"File '{fileName}' has been succesfuly deleted", 2
                else:
                    return f"Cannot delete '{fileName}'. File not found", 2
            else:
                return f"Cannot delete '{fileName}'. File not found", 2


def cd(currentIp, currentPath, requestedDir) -> (str, str, int):
    cursor.execute("select * from directories where ip=? and path=?", (currentIp, currentPath))
    allDirs = cursor.fetchall()
    #  allDirs = str(allDirs).replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("'", "").split(", ")
    newPath = currentPath
    if requestedDir == ".":  # one up
        if currentPath != "":
            oneUpName = currentPath.split("/")
            oneUpName = oneUpName[int(len(oneUpName)-1)]
            # print(oneUpName)
            cursor.execute("select path from directories where ip=? and name=?", (currentIp, oneUpName))
            oneUp = cursor.fetchall()
            newPath = oneUp[0][0]
            if newPath == "":
                show = '""'
            else:
                show = newPath.replace(",)", "")
        else:
            newPath = ""
            show = '""'
    else:
        ok = False
        for i in range(len(allDirs)):
            if requestedDir == allDirs[i][2]:
                if currentPath == "":
                    newPath = requestedDir
                    show = newPath
                    ok = True
                    break
                else:
                    newPath = currentPath+"/"+requestedDir
                    show = newPath
                    ok = True
                    break
            else:
                pass
        if ok != True:
            return currentPath, f"Cannot change path. Invalid path", 2
    return newPath, f"Path changed to: {show}", 2


def cd0(currentIp) -> (str, int):
    return "", f'Path changed to: ""', 2


def mv(currentIp, currentPath, fileName, destination) -> (str, int):
    cursor.execute("select * from directories where ip=? and path=?", (currentIp, destination))
    destin = cursor.fetchall()
    parts = fileName.split(".")
    destinationParts = destination.split("/")
    destFile = destinationParts[len(destinationParts)-1]
    destFileParts = destFile.split(".")
    if len(destFileParts) == 1:
        nameF, extF = destFileParts[0], ''
    elif len(destFileParts) == 2:
        nameF, extF = destFileParts
    else:
        return "Invalid file name", 2

    print(nameF, extF)
    print(parts)

    if len(destin) != 0:
        if len(parts) == 2:
            name = parts[0]
            extension = parts[1]
            cursor.execute("select * from files where ip=? and name=? and extension=? and path=?", (currentIp, name, extension, currentPath))
            file = cursor.fetchone()
            if file is not None:
                content = file[4]
                cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, destination, nameF, extF, content))
                mydb.commit()

                rm(currentIp, currentPath, fileName, True)
                return f"File {fileName} has been successfuly moved to '/{destination}' folder", 2
            else:
                return "File not found", 2
        elif len(parts) == 1:
            name = parts[0]
            cursor.execute("select * from files where ip=? and name=? and extension=? and path=?", (currentIp, name, '', currentPath))
            file = cursor.fetchone()
            if file is not None:
                content = file[4]
                cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, destination, nameF, '', content))
                mydb.commit()

                rm(currentIp, currentPath, fileName, True)
                return f"File {fileName} has been successfuly moved to '/{destination}' folder", 2
            else:
                return "File not found", 2
        else:
            return "Incorrect file name", 2
    else:
        destParts = str(destination).split("/")
        cp = ""
        index = 1
        for dp in destParts:
            if index != len(destParts):
                cursor.execute("select * from directories where name=? and ip=? and path=?", (dp, currentIp, cp))
                dest = cursor.fetchone()
                print(dest)
                if dest == None:
                    cursor.execute("insert into directories values (?, ?, ?)", (currentIp, cp, dp))
                    mydb.commit()
                # else:
                if index == 1:
                    cp += dp
                else:
                    cp += f"/{dp}"
                #    quit(666)
                index += 1
            else:
                dpParts = str(dp).split(".")
                name = dpParts[0]
                ext = ''
                if len(dpParts) > 1:
                    ext = dpParts[1]
                fileNameParts = fileName.split(".")
                cursor.execute("select * from files where ip=? and name=? and extension=? and path=?", (currentIp, fileNameParts[0], fileNameParts[1], currentPath))
                file = cursor.fetchone()
                print(file)
                cont = file[4]
                print(cp)
                cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, cp, nameF, extF, cont))
                mydb.commit()

                rm(currentIp, currentPath, fileName, True)
                return f"File {fileName} has been successfuly moved to '/{cp}' folder", 2


def connect(currentIp, requestedIp) -> (str, str, int):  # modified(works)
    cursor.execute("select * from connections where sourceIp=?", (currentIp, ))
    allIps = cursor.fetchall()
    print(allIps[1][1])

    #allIps = str(allIps).replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("'", "").split(", ")
    #print(allIps)
    #quit(418)

    for i in range(len(allIps)):
        try:
            source, connection1 = allIps[i][0], allIps[i][1]
            if requestedIp == connection1:
                currentIp = connection1

                log = f'@1467_Connection:_from_70.183.159.171'
                cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
                mydb.commit()

                return currentIp, f"Connected to {requestedIp}", 2
                """
                elif requestedIp == connection2:
                    currentIp = connection2
    
                    log = f'@1467_Connection:_from_70.183.159.171'
                    cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
                    mydb.commit()
    
                    return currentIp, f"Connected to {requestedIp}", 2
                """
            elif requestedIp == currentIp:
                return currentIp, f"Requested IP is the same as current IP.\nFailed to connect to {requestedIp}", 3
            #else:
            #    return currentIp, f"Failed to connect to {requestedIp}.\nNo connection found.", 3
        except IndexError:
            pass

    return currentIp, f"Failed to connect to {requestedIp}.\nNo connection found.", 3

    """
    try:
        source, connection1 = allIps[0], allIps[1]
        currentIp = connection1
        return currentIp, f"Connected to {requestedIp}", 2
    except IndexError:
        return currentIp, f"Failed to connect to {requestedIp}", 2
    """


def probe(currentIp) -> (str, int):
    # server variables:
    # 0-ip, 1-name, 2-ssh, 3-ftp, 4-smtp, 5-http, 6-port22, 7-port21, 8-port25, 9-port80, 10-rpfc, 11-proxy, 12-firewall, 13-proxyRequirements, 14-shell, 15-connected, 16-visible, 17-login, 18-password, 19-logged
    cursor.execute("select * from servers where ip=?", (currentIp, ))
    server = cursor.fetchone()
    print(server)
    oprfc = server[10]
    ServerName = server[1]

    isSshLocked = server[2]
    isSshNotHacked = server[6]

    if not isSshLocked:
        sshLocked = "unlocked"
    else:
        sshLocked = "locked"

    if not isSshNotHacked:
        sshHacked = "hacked"
    else:
        sshHacked = "not hacked"

    isFtpLocked = server[3]
    isFtpNotHacked = server[7]

    if not isFtpLocked:
        ftpLocked = "unlocked"
    else:
        ftpLocked = "locked"

    if not isFtpNotHacked:
        ftpHacked = "hacked"
    else:
        ftpHacked = "not hacked"

    isSmtpLocked = server[4]
    isSmtpNotHacked = server[8]

    if not isSmtpLocked:
        smtpLocked = "unlocked"
    else:
        smtpLocked = "locked"

    if not isSmtpNotHacked:
        smtpHacked = "hacked"
    else:
        smtpHacked = "not hacked"

    isHttpLocked = server[5]
    isHttpNotHacked = server[9]

    if not isHttpLocked:
        httpLocked = "unlocked"
    else:
        httpLocked = "locked"

    if not isHttpNotHacked:
        httpHacked = "hacked"
    else:
        httpHacked = "not hacked"

    isProxy = server[11]

    if isProxy:
        proxyBypassed = "Detected"
    else:
        proxyBypassed = "Bypassed"

    isFirewall = server[12]

    if isFirewall:
        firewallBypassed = "Detected"
    else:
        firewallBypassed = "Bypassed"

    output = f"Port#: 22 - SSH                 {sshLocked}      {sshHacked}\n" \
             f"Port#: 21 - FTP Server          {ftpLocked}      {ftpHacked}\n" \
             f"Port#: 25 - SMTP MailServer     {smtpLocked}      {smtpHacked}\n" \
             f"Port#: 80 - HTTP WebServer      {httpLocked}      {httpHacked}\n" \
             f"Firewall {firewallBypassed}\n" \
             f"Proxy {proxyBypassed}\n" \
             f"Open Ports Required for Crack: {oprfc}\n" \
             f"{ServerName} @{currentIp}\n" \
             f"Open ports"
    return output, 10


def exe() -> (str, int):
    cursor.execute("select * from files where ip=? and path=? and extension=?", ("70.183.159.171", "bin", "exe"))
    exeFiles = cursor.fetchall()
    txt = ""
    count = 1
    for f in exeFiles:
        temp = str(f[2]) + "." + str(f[3]) + "\n"
        txt += temp
        count += 1
    if count != 1:
        return txt, count
    else:
        return "No 'exe' file found", 2


def disconnect(currentIp) -> (str, str, str, int): # add proxy and firewall
    cursor.execute("select hasFirewall, hasProxy from servers where ip=?", (currentIp, ))
    hasFirewall, hasProxy = cursor.fetchone()
    print(hasFirewall)
    print(hasProxy)
    cursor.execute("update servers set port22=TRUE, port21=TRUE, port25=TRUE, port80=TRUE, ssh=TRUE, ftp=TRUE, smtp=TRUE, http=TRUE, logged=False, firewall=?, hasProxy=? where ip=?", (hasFirewall, hasProxy, currentIp))
    cursor.execute("update servers set connected=FALSE where ip=?", (currentIp, ))
    cursor.execute("update servers set connected=TRUE, logged=TRUE where ip='70.183.159.171'")
    mydb.commit()
    curIp = str(currentIp).replace(',)', '')
    curPath = ""

    log = f'@1496_70.183.159.171_Disconnected'
    cursor.execute("insert into files values (?, ?, ?, ?, ?)", (curIp, 'log', log, '', log))
    mydb.commit()

    return "70.183.159.171", curPath, f'Connected to 70.183.159.171\nDisconnected from: {curIp}', 3


def cat(currentIp, filename) -> (str, int):
    try:
        name, ext = str(filename).split(".")  # 2-name, 3-ext, 4-con
        cursor.execute("select * from files where ip=?", (currentIp,))
        files = cursor.fetchall()
        ok = False
        output = ""
        for f in files:
            if f"{f[2]}.{f[3]}" == filename:
                lines = f[4].split("\n")
                print(len(lines), lines)
                count = len(lines)
                ok = True
                for i in reversed(range(len(lines))):
                    output += lines[i]
                    if i != 0:
                        output += "\n"
                break
        if ok == True:
            log = f'@1534_FileRead:_by_70.183.159.171_-_file:{name}.{ext}'
            cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
            mydb.commit()
            return output, count+1
        else:
            return f"File {filename} not found", 2
    except ValueError:
        cursor.execute("select * from files where ip=?", (currentIp, ))
        files = cursor.fetchall()
        ok = False
        output = ""
        for f in files:
            if f[2] == filename:
                lines = f[4].split("\n")
                count = len(lines)
                ok = True
                for i in reversed(range(len(lines))):
                    output += lines[i]
                    if i != 0:
                        output += "\n"
                break
    if ok == True:
        log = f'@1534_FileRead:_by_70.183.159.171_-_file:{filename}'
        cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
        mydb.commit()
        return output, count+1
    else:
        return f"File {filename} not found", 2


def repl(content, text, replacement) -> str:  # my very own replace command(I can't believe it works :D)
    content = content[0]
    altContent = ""
    l = len(str(text))
    index = 0
    for i in range(len(content) - (l-1)):
        #if index + l + 1 > len(content):
        #    break

        check = ""
        for j in range(l):
            content = str(content)

            if index + j > len(content)-l:
                break

            check = check + content[index+j]
        if check == text:
            altContent = altContent + replacement
            index += l
        else:
            if index < len(content):
                altContent = altContent + content[index]
                index += 1

    return altContent


def replace(currentIp, currentPath, filename, text, replacement) -> (str, int):  # it works :D
    parts = str(filename).split('.')
    if len(parts) == 2:
        n, e = parts
    else:
        n, e = parts, ""
    cursor.execute("select content from files where ip=? and path=? and name=? and extension=?", (currentIp, currentPath, n, e)) # ip, path, name, extension, content
    content = cursor.fetchone()
    ok = False
    if content is not None:
        ok = True
    if not ok:
        return f"File '{filename}' not found", 2
    else:
        print(content)
        # content = str(content).replace(text, replacement)
        content = repl(content, text, replacement)
        print(content)
        cursor.execute("update files set content=? where ip=? and path=? and name=? and extension=?", (content, currentIp, currentPath, n, e))
        mydb.commit()

        log = f'@1543_FileChanged:_by_70.183.159.171_-_file:{filename}'
        cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
        mydb.commit()

    return f"Altered file: '{filename}'", 2


def genRandLet() -> str:  # used in analyze
    letter = str(choice(ascii_letters))
    return letter


def analyze(currentIp, lvl) -> (str, int, int):  # done in a train, on a phone
    cursor.execute("select firewallPassword from servers where ip=?", (currentIp, ))
    password = cursor.fetchone()[0]
    passwordParts = []
    for i in range(6):
        passwordParts.append(password[i])

    print(passwordParts)

    if lvl == 6:
        rows = ""
        for i in reversed(range(6)):
            pwdInd = randint(0, 19)
            for j in range(20):
                if j == pwdInd:
                    rows += passwordParts[i]
                    rows += " "
                else:
                    rows += genRandLet()
                    rows += " "
            rows += "\n"
        return rows, 7, 5

    elif lvl == 5:
        rows = ""
        for i in reversed(range(6)):
            pwdInd = randint(0, 19)
            zeros = []
            while True:
                zeroIndex = randint(0, 19)
                if zeroIndex != pwdInd and zeros.__contains__(zeroIndex) == False:
                    zeros.append(zeroIndex)

                if len(zeros) == 4:
                    break

            print(zeros)
            for j in range(20):
                if j == pwdInd:
                    rows += passwordParts[i]
                    rows += " "
                else:
                    isZero = False
                    for z in zeros:
                        if j == z:
                            rows += "0"
                            rows += " "
                            isZero = True
                            break
                    if isZero != True:
                        rows += genRandLet()
                        rows += " "
            rows += "\n"
        return rows, 7, 4

    elif lvl == 4:
        rows = ""
        for i in reversed(range(6)):
            pwdInd = randint(0, 19)
            zeros = []
            while True:
                zeroIndex = randint(0, 19)
                if zeroIndex != pwdInd and zeros.__contains__(zeroIndex) == False:
                    zeros.append(zeroIndex)

                if len(zeros) == 8:
                    break

            print(zeros)
            for j in range(20):
                if j == pwdInd:
                    rows += passwordParts[i]
                    rows += " "
                else:
                    isZero = False
                    for z in zeros:
                        if j == z:
                            rows += "0"
                            rows += " "
                            isZero = True
                            break
                    if isZero != True:
                        rows += genRandLet()
                        rows += " "
            rows += "\n"
        return rows, 7, 3

    elif lvl == 3:
        rows = ""
        for i in reversed(range(6)):
            pwdInd = randint(0, 19)
            zeros = []
            while True:
                zeroIndex = randint(0, 19)
                if zeroIndex != pwdInd and zeros.__contains__(zeroIndex) == False:
                    zeros.append(zeroIndex)

                if len(zeros) == 12:
                    break

            print(zeros)
            for j in range(20):
                if j == pwdInd:
                    rows += passwordParts[i]
                    rows += " "
                else:
                    isZero = False
                    for z in zeros:
                        if j == z:
                            rows += "0"
                            rows += " "
                            isZero = True
                            break
                    if isZero != True:
                        rows += genRandLet()
                        rows += " "
            rows += "\n"
        return rows, 7, 2

    elif lvl == 2:
        rows = ""
        for i in reversed(range(6)):
            pwdInd = randint(0, 19)
            zeros = []
            while True:
                zeroIndex = randint(0, 19)
                if zeroIndex != pwdInd and zeros.__contains__(zeroIndex) == False:
                    zeros.append(zeroIndex)

                if len(zeros) == 16:
                    break

            print(zeros)
            for j in range(20):
                if j == pwdInd:
                    rows += passwordParts[i]
                    rows += " "
                else:
                    isZero = False
                    for z in zeros:
                        if j == z:
                            rows += "0"
                            rows += " "
                            isZero = True
                            break
                    if isZero != True:
                        rows += genRandLet()
                        rows += " "
            rows += "\n"
        return rows, 7, 1

    elif lvl == 1:
        rows = ""
        for i in reversed(range(6)):
            pwdInd = randint(0, 19)
            zeros = []
            while True:
                zeroIndex = randint(0, 19)
                if zeroIndex != pwdInd and zeros.__contains__(zeroIndex) == False:
                    zeros.append(zeroIndex)

                if len(zeros) == 19:
                    break

            print(zeros)
            for j in range(20):
                if j == pwdInd:
                    rows += passwordParts[i]
                    rows += " "
                else:
                    isZero = False
                    for z in zeros:
                        if j == z:
                            rows += "0"
                            rows += " "
                            isZero = True
                            break
                    if isZero != True:
                        rows += genRandLet()
                        rows += " "
            rows += "\n"
        return rows, 7, 1


def solve(currentIp, password) -> (str, int):  # not finished
    cursor.execute("select firewall, firewallPassword from servers where ip=?", (currentIp, ))
    isFirewallEnabled, firewallPassord = cursor.fetchone()

    if isFirewallEnabled == False:
        return "Firewall not detected", 2
    else:
        if password == firewallPassord:
            cursor.execute("update servers set firewall=False where ip=?", (currentIp, ))
            mydb.commit()
            return "Firewall disabled", 2
        else:
            return "Incorrect password\nFailed to disable firewall", 3


def login(currentIp, username, password) -> (str, int):  # it will send request login/password/enter(go on)  it didn't work :(
    cursor.execute("select login, password, logged from servers where ip=?", (currentIp, ))
    user, pwd, isLogged = cursor.fetchone()
    if not isLogged:
        if username == user and password == pwd:
            cursor.execute("update servers set logged=True where ip=?", (currentIp, ))
            mydb.commit()

            log = f'@1496_70.183.159.171_Became_Admin'
            cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
            mydb.commit()

            return "Logged in as an administrator", 2
        else:
            return "Incorrect login and/or password", 2
    else:
        return "The user is already logged in\nCannot log in", 3


def loginTry(currentIp, currentPath, oldPath, username, password) -> (str, int):
    if currentPath == oldPath:
        return oldPath
    elif currentPath == "login:" and username is not None:
        return username
    elif currentPath == "password:" and password is not None:
        cursor.execute("select login, password from servers where ip=?", (currentIp, ))
        corLog, corPwd = cursor.fetchone()
        if username == corLog and password == corPwd:
            cursor.execute("update servers set logged=True where ip=?", (currentIp, ))
            mydb.commit()

            log = f'@1496_70.183.159.171_Became_Admin'
            cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
            mydb.commit()

            return "Logged in as an administrator", 2
        return "Incorrect login/password", 2


def upload(currentIp, fileName, currentPath) -> (str, int):
    destin = fileName.split("/")
    count = len(destin)
    if count > 1:
        destinParts = ""
        for i in range(count-1):
            destinParts += destin[i]
        file = destin[count-1]
        fileParts = file.split(".")
        if len(fileParts) == 2:
            name = fileParts[0]
            ext = fileParts[1]
        else:
            name = fileParts[0]
            ext = ""
        cursor.execute("select content from files where ip=? and name=? and extension=? and path=?", ("70.183.159.171", name, ext, destinParts))
        f = cursor.fetchone()
        if f is None:
            return f"File has not been found\nCannot upload file {fileName}", 3
        else:
            cursor.execute("insert into files values(?, ?, ?, ?, ?)", (currentIp, currentPath, name, ext, f[0]))
            mydb.commit()

            log = f'@1564_FileUploaded:_by_70.183.159.171_-_file:{name}'
            cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
            mydb.commit()

            return f"File {fileName} has been uploaded to {currentPath}", 2
    else:
        fileParts = fileName.split(".")
        if len(fileParts) == 2:
            name, ext = fileParts
        else:
            name = fileParts[0]
            ext = ""
        cursor.execute("select content from files where ip=? and name=? and extension=? and path=?", ("70.183.159.171", name, ext, ""))
        f = cursor.fetchone()
        if f is None:
            return f"File has not been found\nCannot upload file {fileName}", 3
        else:
            cursor.execute("insert into files values(?, ?, ?, ?, ?)", (currentIp, currentPath, name, ext, f[0]))
            mydb.commit()

            log = f'@1564_FileUploaded:_by_70.183.159.171_-_file:{name}.{ext}'
            cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
            mydb.commit()

            return f"File {fileName} has been uploaded to {currentPath}", 2


def append(currentIp, currentPath, filename, data) -> (str, int):  # simple append one word
    nameParts = str(filename).split('.')
    if len(nameParts) == 2:
        name, ext = nameParts
    elif len(nameParts) == 1:
        name, ext = nameParts, ''
    else:
        return "Incorrect filename", 2

    cursor.execute("select * from files where ip=? and name=? and extension=? and path=?", (currentIp, name, ext, currentPath))
    file = cursor.fetchone()

    if len(file) == 0:
        return f"File {filename} not found", 2
    else:
        content = str(file[4])
        data = str(data)
        content = content + '\n' + data
        print(content)
        cursor.execute("update files set content=? where ip=? and name=? and extension=? and path=?", (content, currentIp, name, ext, currentPath))
        mydb.commit()

        log = f'@1552_FileAppended:_by_70.183.159.171_-_file:{name}.{ext}'
        cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
        mydb.commit()

        return f"Appended file {filename} with data: {data}", 2


def shell(currentIp) -> (str, int):
    cursor.execute("select shell from servers where ip=?", (currentIp, ))
    isShelled = cursor.fetchone()[0]
    print(isShelled)
    if not isShelled:
        cursor.execute("update servers set shell=True where ip=?", (currentIp, ))
        mydb.commit()
        return "Shell created", 2
    else:
        return "Shell has already been created", 2


def overload(currentIp) -> (str, int):  # not finished
    cursor.execute("select shell from servers")
    isShelled = cursor.fetchall()
    count = 0
    for i in range(len(isShelled)):
        if isShelled[i][0]==True:
            count += 1
    cursor.execute("select proxyRequirements from servers where ip=?", (currentIp, ))
    proxyRequirements = cursor.fetchone()
    if count < proxyRequirements[0]:
        return f"Shells needed: {proxyRequirements[0]}\nYou don't have enough shells created.", 3
    else:
        cursor.execute("update servers set proxy=False where ip=?", (currentIp, ))
        return f"Proxy bypassed", 2


def quitGame() -> None:
    cursor.execute("select hasFirewall, hasProxy from servers where ip=?", (currentIp,))
    hasFirewall, hasProxy = cursor.fetchone()
    print(hasFirewall)
    print(hasProxy)
    cursor.execute("update servers set port22=TRUE, port21=TRUE, port25=TRUE, port80=TRUE, ssh=TRUE, ftp=TRUE, smtp=TRUE, http=TRUE, logged=False, shell=False, firewall=?, proxy=? where ip=?", (hasFirewall, hasProxy, currentIp))
    cursor.execute("delete from usedCommands")
    mydb.commit()
    mydb.close()
    quit(0)


def sshCrack(currentIp, SSHcrack):  # finished
    cursor.execute("select name, extension, content from files where ip='70.183.159.171'")
    files = cursor.fetchall()
    cursor.execute("select ssh, firewall, proxy from servers where ip=?", (currentIp, ))
    sshLocked, firewall, proxy = cursor.fetchone()
    found = False
    for f in files:
        if f[0] == 'SSHcrack' and f[1] == 'exe' and f[2] == SSHcrack:  # it's ok
            found = True
            break

    if not found:
        return "Required file 'SSHcrack.exe': modified/missing", 2
    else:
        if firewall:
            return "Action blocked by firewall", 2
        elif proxy:
            return "Action blocked by proxy", 2
        elif not sshLocked:
            return "Port 22 has already been unlocked", 2
        else:
            cursor.execute("update servers set ssh=? where ip=?", (False, currentIp))
            mydb.commit()
            return "Successfully unlocked port 22", 2


def ftpBounce(currentIp, FTPBounce):
    cursor.execute("select name, extension, content from files where ip='70.183.159.171'")
    files = cursor.fetchall()
    cursor.execute("select ftp, firewall, proxy from servers where ip=?", (currentIp, ))
    ftpLocked, firewall, proxy = cursor.fetchone()
    found = False
    for f in files:
        if f[0] == 'FTPBounce' and f[1] == 'exe' and f[2] == FTPBounce:
            found = True
            break

    if not found:
        return "Required file 'FTPBounce.exe': modified/missing", 2
    else:
        if firewall:
            return "Action blocked by firewall", 2
        elif proxy:
            return "Action blocked by proxy", 2
        elif not ftpLocked:
            return "Port 21 has already been unlocked", 2
        else:
            cursor.execute("update servers set ftp=? where ip=?", (False, currentIp))
            mydb.commit()
            return "Successfully unlocked port 21", 2


def smtpOverflow(currentIp, SMTPoverflow):
    cursor.execute("select name, extension, content from files where ip='70.183.159.171'")
    files = cursor.fetchall()
    cursor.execute("select smtp, firewall, proxy from servers where ip=?", (currentIp, ))
    smtpLocked, firewall, proxy = cursor.fetchone()
    found = False
    for f in files:
        if f[0] == 'SMTPoverflow' and f[1] == 'exe' and f[2] == SMTPoverflow:
            found = True
            break

    if not found:
        return "Required file 'SMTPoverflow.exe': modified/missing", 2
    else:
        if firewall:
            return "Action blocked by firewall", 2
        elif proxy:
            return "Action blocked by proxy", 2
        elif not smtpLocked:
            return "Port 25 has already been unlocked", 2
        else:
            cursor.execute("update servers set smtp=? where ip=?", (False, currentIp))
            mydb.commit()
            return "Successfully unlocked port 25", 2


def webServerWorm(currentIp, WebServerWorm):
    cursor.execute("select name, extension, content from files where ip='70.183.159.171'")
    files = cursor.fetchall()
    cursor.execute("select http, firewall, proxy from servers where ip=?", (currentIp, ))
    httpLocked, firewall, proxy = cursor.fetchone()
    found = False
    for f in files:
        if f[0] == 'WebServerWorm' and f[1] == 'exe' and f[2] == WebServerWorm:
            found = True
            break

    if not found:
        return "Required file 'WebServerWorm.exe': modified/missing", 2
    else:
        if firewall:
            return "Action blocked by firewall", 2
        elif proxy:
            return "Action blocked by proxy", 2
        elif not httpLocked:
            return "Port 80 has already been unlocked", 2
        else:
            cursor.execute("update servers set http=? where ip=?", (False, currentIp))
            mydb.commit()
            return "Successfully unlocked port 80", 2


def porthack(currentIp, requestedPort) -> (str, int):  # should be ok
    cursor.execute("select rpfc from servers where ip=?", (currentIp, ))
    rpfc = cursor.fetchone()
    cursor.execute("select ssh, ftp, smtp, http from servers where ip=?", (currentIp, ))
    secur = cursor.fetchall()
    cursor.execute("select port22, port21, port25, port80 from servers where ip=?", (currentIp,))
    ports = cursor.fetchall()

    unlockedPortsCount = 0

    for s in range(len(secur[0])):
        if secur[0][s] == False:
            unlockedPortsCount += 1
        else:
            print(":(")
    print(unlockedPortsCount)

    if requestedPort == '22':
        if unlockedPortsCount >= rpfc[0]:
            if ports[0][0] == True:
                time.sleep(3)
                cursor.execute("update servers set port22=FALSE where ip=?", (currentIp, ))
                mydb.commit()
                return "Port 22: hacked successfully", 2
            else:
                return "Port 22: hack failed. Port has already been hacked", 2
        else:
            return "Port 22: hack failed. You didn't open enough ports", 2

    elif requestedPort == '21':
        if unlockedPortsCount >= rpfc[0]:
            if ports[0][1] == True:
                time.sleep(6)
                cursor.execute("update servers set port21=FALSE where ip=?", (currentIp, ))
                mydb.commit()
                return "Port 21: hacked successfully", 2
            else:
                return "Port 21: hack failed. Port has already been hacked", 2
        else:
            return "Port 21: hack failed. You didn't open enough ports", 2

    elif requestedPort == '25':
        if unlockedPortsCount >= rpfc[0]:
            if ports[0][2] == True:
                time.sleep(9)
                cursor.execute("update servers set port25=FALSE where ip=?", (currentIp, ))
                mydb.commit()
                return "Port 25: hacked successfully", 2
            else:
                return "Port 25: hack failed. Port has already been hacked", 2
        else:
            return "Port 25: hack failed. You didn't open enough ports", 2

    elif requestedPort == '80':
        if unlockedPortsCount >= rpfc[0]:
            if ports[0][3] == True:
                time.sleep(12)
                cursor.execute("update servers set port80=FALSE where ip=?", (currentIp, ))
                mydb.commit()
                return "Port 80: hacked successfully", 2
            else:
                return "Port 80: hack failed. Port has already been hacked", 2
        else:
            return "Port 80: hack failed. You didn't open enough ports", 2

    else:
        return f"Port {requestedPort}: hack failed. Invalid port number", 2


def resetDB(cursor, mydb) -> None:
    mydb.close()
    os.remove("hacknetrecreation.db")
    #cursor.execute("drop table connections")
    #cursor.execute("drop table servers")
    #cursor.execute("drop table emails")
    #cursor.execute("drop table files")
    #cursor.execute("drop table directories")
    #cursor.execute("drop table usedCommands")
    #mydb.commit()


def ls(currentIp, currentPath) -> (str, int):  # probably finished
    cursor.execute("select * from directories where ip=? and path=?", (currentIp, currentPath))
    currentDirectories = cursor.fetchall()  # indexes 1-path, 2-dir name
    cursor.execute("select * from files where ip=? and path=?", (currentIp, currentPath))  # ip, path, name, exten, cont
    currentFiles = cursor.fetchall()
    out = ""
    for i in range(len(currentFiles)):
        out += f"    {currentFiles[i][2]}.{currentFiles[i][3]}\n"
    for i in range(len(currentDirectories)):
        out += f"    /{currentDirectories[i][2]}\n"
    out += f"/{currentPath}\n"
    return out, len(currentDirectories)+len(currentFiles)+2


def buildTree(currentIp):
    cursor.execute("select * from directories where ip=?", (currentIp, ))
    directories = cursor.fetchall()

    cursor.execute("select * from files where ip=?", (currentIp, ))
    files = cursor.fetchall()

    tree = {}
    # Process directories
    for ip, path, name in directories:
        if ip == currentIp:
            current_dict = tree
            for part in path.split('/'):
                if part:
                    current_dict = current_dict.setdefault(part, {})
            current_dict[name] = {}

    # Process files
    for ip, path, name, extension, content in files:
        if ip == currentIp:
            current_dict = tree
            for part in path.split('/'):
                if part:
                    current_dict = current_dict.setdefault(part, {})
            if len(extension) > 0:
                file_name_with_extension = f"{name}.{extension}"
            else:
                file_name_with_extension = f"{name}"
            current_dict[file_name_with_extension] = {'content': content}

    return tree


def print_tree(tree, current_path, prefix='', tree_array=None):
    if tree_array is None:
        tree_array = []

    if current_path:
        path_parts = current_path.split('/')
        for part in path_parts[:-1]:
            if part in tree:
                tree = tree[part]
            else:
                print("Path not found.")
                return
        last_part = path_parts[-1]
        if last_part in tree:
            tree = {last_part: tree[last_part]}
        else:
            print("Path not found.")
            return

    for name, value in tree.items():
        if isinstance(value, dict):
            tree_array.append(f"{prefix}|-- {name}")
            print_tree(value, '', prefix + '|   ', tree_array)
        elif isinstance(value, str):
            pass
        else:
            tree_array.append(f"{prefix}|-- {name}")

    reversedTree = ""
    for i in reversed(range(len(tree_array))):
        reversedTree += (tree_array[i] + "\n")

    return reversedTree, len(tree_array)+1


def nano2(currentIp, currentPath, filename, content, oldPath, exists):  # it works
    print(filename)
    filenameParts = str(filename).split(".")
    if len(filenameParts) == 2:
        name, ext = filenameParts
    elif len(filenameParts) == 1:
        name, ext = filenameParts[0], ""

    if not exists:
        cursor.execute("insert into files values(?, ?, ?, ?, ?)", (currentIp, oldPath, name, ext, content))
        mydb.commit()
        log = f'@1566_FileCreated:_by_70.183.159.171_-_file:{name}.{ext}'
    else:
        cursor.execute("update files set content=? where ip=? and path=? and name=? and extension=?", (content, currentIp, oldPath, name, ext))
        mydb.commit()
        log = f'@1568_FileModified:_by_70.183.159.171_-_file:{name}.{ext}'

    cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
    mydb.commit()

    if not exists:
        return f"File '{filename}' has been successfully created in {oldPath}", 2
    else:
        return f"File '{filename}' has been successfully modified", 2


def nano1(currentIp, currentPath, filename, content, oldPath):  # it works
    print(filename)
    filenameParts = str(filename).split(".")
    if len(filenameParts) == 2:
        name, ext = filenameParts
    elif len(filenameParts) == 1:
        name, ext = filenameParts[0], ""
    else:
        return f"Incorrect file name\nCannot create file '{filename}'", 3

    cursor.execute("select * from files where ip=? and path=? and name=? and extension=?", (currentIp, oldPath, name, ext))
    file = cursor.fetchall()
    if len(file) == 0:  # new file
        return oldPath, filename, False, ''
    else:  # existing file
        return oldPath, filename, True, file[0][4]


def nanoOld(currentIp, currentPath, filename, content, oldPath):  # @1568_FileModified:_by_70.183.159.171_-_file:filename.ext  <- delete
    print(filename)
    filenameParts = str(filename).split(".")
    if len(filenameParts) == 2:
        name, ext = filenameParts
    elif len(filenameParts) == 1:
        name, ext = filenameParts[0], ""
    else:
        return f"Incorrect file name\nCannot create file '{filename}'", 3
    cursor.execute("select * from files where ip=? and path=? and name=? and extension=?", (currentIp, oldPath, name, ext))
    file = cursor.fetchall()
    if len(file) != 0:  # not working correctly
        #return "", 2
        return f"File '{filename}' already exists in {oldPath}", 2  # for now
    else:
        if content is None:
            return oldPath, filename
        else:
            cursor.execute("insert into files values(?, ?, ?, ?, ?)", (currentIp, oldPath, name, ext, content))
            mydb.commit()

            log = f'@1566_FileCreated:_by_70.183.159.171_-_file:{name}.{ext}'
            cursor.execute("insert into files values (?, ?, ?, ?, ?)", (currentIp, 'log', log, '', log))
            mydb.commit()

            return f"File '{filename}' has been successfully created in {oldPath}", 2


mydb.commit()
# pygame
pg.init()

# colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# set up the pygame window
width, height = 800, 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption('Hacknet Terminal Recreation')

# font settings
font = pg.font.Font(None, 20)
command = ''


# starting values(every time the game is launched)
currentIp = "70.183.159.171"
currentPath = ""
oldPath = None
fileName = None
exists = False
username = ""
password = ""
lvl = 6  # firewall lvl
cursor.execute("update servers set logged=True where ip=?", (currentIp, ))
mydb.commit()
cursor.execute("select * from usedCommands")
var = cursor.fetchall()
currentIndex = 0
SSHcrack = "110111000110111010001000001111000111110001000001100110110011100010100110101\n011111010010011100011101010100111010110110111100111000101001100010010010111\n110000010000010110100001110101100000110110011010001100010111010101101010111\n110110010111110111001111110011001010111010000111010001001001111100100100110\n100110101101101010110111110111111010000000001001110111001111111101010110000\n11011110110001111111010101110"
FTPBounce = ""  # fill later
SMTPoverflow = ""  # fill later
WebServerWorm = ""  # fill later


running = True
while running:

    number = 0
    screen.fill(black)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            cursor.execute("delete from usedCommands")
            mydb.commit()
            quitGame()
        elif event.type == pg.KEYDOWN:  # add for 'arrow up/down'
            if event.key == pg.K_RETURN:  # not finished
                # execute command
                command = str(command)
                output = ''  # When command is being executed set output(expected value). IMPORTANT!!!!!!
                prevPath = currentPath

                #  handle unique inputs
                if currentPath == "login:":
                    username = loginTry(currentIp, currentPath, oldPath, command, None)
                    currentPath = "password:"
                elif currentPath == "password:":
                    output, number = loginTry(currentIp, currentPath, oldPath, username, command)
                    currentPath = oldPath
                    command = "login"  # if it's not here it will print typed password as command
                    cursor.execute("insert into usedCommands (command, printout, linesCount, currentCommandPath) values (?, ?, ?, ?)", (command, output, number, prevPath))  # !!!!!
                    mydb.commit()
                elif currentPath == "file content:":
                    output, number = nano2(currentIp, currentPath, fileName, command, oldPath, exists)
                    exists = False
                    currentPath = oldPath
                    cursor.execute("insert into usedCommands (command, printout, linesCount, currentCommandPath) values (?, ?, ?, ?)", (command, output, number, prevPath))  # !!!!!
                    mydb.commit()
                else:
                    #  handle commands
                    if len(command.split()) == 1:
                        if command == "quit":
                            quitGame()
                        elif command == "resetDB":
                            resetDB(cursor, mydb)
                            quit(666)
                        elif command == "scan":
                            output, number = scan(currentIp)
                        elif command == "ls":
                            output, number = ls(currentIp, currentPath)
                        elif command == "cd":
                            currentPath, output, number = cd0(currentIp)
                        elif command == "disconnect" or command == "dc":
                            lvl = 6
                            currentIp, currentPath, output, number = disconnect(currentIp)
                        elif command == "probe":
                            output, number = probe(currentIp)
                        elif command == "exe":
                            output, number = exe()
                        elif command == "tree":
                            treee = buildTree(currentIp)
                            output, number = print_tree(treee, currentPath)
                        elif command == "analyze":
                            output, number, lvl = analyze(currentIp, lvl)
                        elif command == "shell":
                            output, number = shell(currentIp)
                        elif command == "overload":
                            output, number = overload(currentIp)
                        elif command == "login":
                            oldPath = loginTry(currentIp, currentPath, currentPath, None, None)
                            currentPath = "login:"
                        else:
                            output, number = f"No command: '{command}' - Check Syntax", 2
                        # add to db
                        cursor.execute("insert into usedCommands (command, printout, linesCount, currentCommandPath) values (?, ?, ?, ?)", (command, output, number, prevPath))  # !!!!!
                        mydb.commit()

                    elif len(command.split()) == 2:
                        # print(command.split())
                        txt1, txt2 = command.split()
                        if command == f"help {txt2}":
                            output, number = help(txt2)
                        elif command == f"connect {txt2}":
                            lvl = 6
                            currentIp, output, number = connect(currentIp, txt2)
                        elif command == f"cd {txt2}":
                            currentPath, output, number = cd(currentIp, currentPath, txt2)
                        elif command == f"porthack {txt2}":
                            output, number = porthack(currentIp, txt2)
                        elif command == f"cat {txt2}":
                            output, number = cat(currentIp, txt2)
                        elif command == f"rm {txt2}":
                            output, number = rm(currentIp, currentPath, txt2)
                        elif command == f"scp {txt2}":
                            output, number = scp(currentIp, currentPath, txt2)
                        elif command == f"solve {txt2}":
                            output, number = solve(currentIp, txt2)
                        elif command == f"upload {txt2}":
                            output, number = upload(currentIp, txt2, currentPath)
                        elif command == f"nano {txt2}":
                            oldPath, fileName, exists, command = nano1(currentIp, currentPath, txt2, None, currentPath)
                            currentPath = "file content:"
                        elif command == "sshcrack 22":
                            output, number = sshCrack(currentIp, SSHcrack)
                        elif command == "ftpbounce 21":
                            output, number = ftpBounce(currentIp, FTPBounce)
                        elif command == "smtpoverflow 25":
                            output, number = smtpOverflow(currentIp, SMTPoverflow)
                        elif command == "webserverworm 80":
                            output, number = webServerWorm(currentIp, WebServerWorm)
                        else:
                            output, number = f"No command: '{command}' - Check Syntax", 2
                        # add to db
                        cursor.execute("insert into usedCommands (command, printout, linesCount, currentCommandPath) values (?, ?, ?, ?)", (command, output, number, prevPath))  # !!!!!
                        mydb.commit()

                    elif len(command.split()) == 3:
                        txt1, txt2, txt3 = command.split()
                        if command == f"scp {txt2} {txt3}":
                            output, number = scp2(currentIp, currentPath, txt2, txt3)
                        elif command == f"login {txt2} {txt3}":
                            output, number = login(currentIp, txt2, txt3)
                        elif command == f"mv {txt2} {txt3}":
                            output, number = mv(currentIp, currentPath, txt2, txt3)
                        elif command == f"append {txt2} {txt3}":
                            output, number = append(currentIp, currentPath, txt2, txt3)
                        else:
                            output, number = f"No command: '{command}' - Check Syntax", 2
                        print("Not added yet")
                        # add to db
                        cursor.execute("insert into usedCommands (command, printout, linesCount, currentCommandPath) values (?, ?, ?, ?)", (command, output, number, prevPath))  # !!!!!
                        mydb.commit()

                    elif len(command.split()) == 4:
                        txt1, txt2, txt3, txt4 = command.split()
                        output, number = replace(currentIp, currentPath, txt2, txt3, txt4)
                        # add to db
                        cursor.execute("insert into usedCommands (command, printout, linesCount, currentCommandPath) values (?, ?, ?, ?)", (command, output, number, prevPath))  # !!!!!
                        mydb.commit()

                    else:
                        output, number = f"No command: '{command}' - Check Syntax", 2
                        # add to db
                        cursor.execute("insert into usedCommands (command, printout, linesCount, currentCommandPath) values (?, ?, ?, ?)", (command, output, number, prevPath))  # !!!!!
                        mydb.commit()
                # not finished
                #cursor.execute("insert into usedCommands (command, printout, linesCount, currentCommandPath) values (?, ?, ?, ?)", (command, output, number, prevPath))# !!!!!
                #mydb.commit()
                if not exists:
                    command = ''

                cursor.execute("select command from usedCommands")
                var = cursor.fetchall()
                currentIndex = len(var)
            elif event.key == pg.K_UP:
                if currentIndex > 0:
                    currentIndex -= 1
                    command = var[currentIndex][0]
            elif event.key == pg.K_DOWN:
                if currentIndex < len(var)-1:
                    currentIndex += 1
                    command = var[currentIndex][0]
            elif event.key == pg.K_BACKSPACE:
                # Remove last character from input command
                command = command[:-1]
            else:
                command += event.unicode  # Add typed characters to input command

    # Render input command
    cursor.execute("select command from usedCommands")
    used = cursor.fetchall()
    cursor.execute("select printout from usedCommands")
    output = cursor.fetchall()
    cursor.execute("select linesCount from usedCommands")
    number = cursor.fetchall()
    cursor.execute("select currentCommandPath from usedCommands")
    paths = cursor.fetchall()

    totalNum = 0
    out = []
    lengths = []

    allNum = 0
    for i in reversed(range(int(len(used)))):
        num = int(str(number[len(output) - 1 - i]).replace('(', '').replace(',)', ''))
        totalNum += num
        for j in reversed(range(num-1)):
            txt = str(output[len(output) - 1 - i]).replace('")', '').replace('("', '').replace("',)", "").replace("('", "")
            txt = txt.replace('\\n', '\n').split('\n')
            out.append(txt[j])

    for i in range(int(len(used))):
        num = int(str(number[len(output) - 1 - i]).replace('(', '').replace(',)', ''))
        lengths.append(num-1+allNum)
        allNum += num
    # print(totalNum)
    # print(len(out))  # totalNum-1

    index = len(out)-1
    c = len(used)-1
    print(lengths)
    for i in range(totalNum):
        if lengths.__contains__(i):
            currentCommand = str(used[c]).replace('(', '').replace(',)', '').replace("'", "")
            input_surface = font.render(f'{paths[c][0]}> ' + currentCommand, True, green)  # path is ok :)
            screen.blit(input_surface, (10, height - 45 - (20 * (i + 1))))
            c -= 1
        else:
            print(i, " ", index)
            input_surface = font.render(out[index], True, white)
            screen.blit(input_surface, (10, height - 45 - (20*(i+1))))
            index -= 1

    input_surface = font.render(f'{currentPath}> ' + command + '_', True, green)  # 45
    screen.blit(input_surface, (10, height - 25))

    pg.display.flip()
