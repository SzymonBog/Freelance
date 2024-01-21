import os
from time import sleep


def main():
    program = True
    companies = []
    d = 0

    class user:
        def __init__(self, name, surname, admin=False, position="Employee"):
            self.name = name
            self.surname = surname
            self.admin = admin
            self.login = None
            self.password = None
            self.logged = False
            self.position = position
            self.payout = 3000.00
            self.task = None
            self.taskToCheck = [] # list of tasks users sent to owner to check
            self.usersWhoSentTask = []
            self.receivedTask = None # notification about receiving a task
            self.firedNotif = None
            self.report = None
            #self.firedUsers = []  used to store them till first login

    class company:
        def __init__(self, companyName: str):
            self.companyName = companyName
            self.users = []
            self.positions = ["Employee", "Expert", "Coordinator", "Team leader", "Head of department",
                              "CEO"]
            self.payouts = [3000.00, 4500.00, 6500.00, 9000.00, 12000.00, 24000.00]

        def addUser(self):
            canAdd = False
            for u in self.users:
                if u.logged == True and u.admin == True:
                    #print(u.name)
                    canAdd = True
                    break
            if canAdd == True:
                os.system('cls')
                print("Add new user:\n")
                success = True
                name = str(input("Name: "))
                surname = str(input("Surname: "))
                #adminint = int(input("Is admin(1 or 0): "))
                adminstr = str(input("Is admin('yes' or 'no'): "))
                for u in self.users:
                    if u.surname == surname:
                        if u.name == name:
                            print("User {} {} already exists.".format(name, surname))
                            success = False
                            break
                if success == True:
                    #if adminint == 1:
                    if adminstr == "yes":
                        admin = True
                        ok = True
                    #elif adminint == 0:
                    elif adminstr == 'no':
                        admin = False
                        ok = True
                    else:
                        ok = False
                    if ok == True:
                        self.users.append(user(name, surname, admin))
                        print("New user added\n")
                    else:
                        print("Wrong value\n")
            else:
                print("You don't have clearance to add new users\n")
            sleep(5)

        def setLoginAndPassword(self):
            canChange = False
            for u in self.users:
                if u.logged == True and u.admin == True:
                    canChange = True
                    break
            if canChange == True:
                os.system('cls')
                print("Set login and password")
                ok = False
                name = str(input("Name: "))
                surname = str(input("Surname: "))
                for u in self.users:
                    if u.name == name and u.surname == surname:
                        u.login = str(input("Set login: "))
                        u.password = str(input("Set password: "))
                        print("Login and password for {} {} is set".format(u.name, u.surname))
                        ok = True
                        break
                if ok == False:
                    print("User {} {} doesn't exist.\n".format(name, surname))
            sleep(5)
            return None

        def increaseOrDecreasePayout(self):
            canChange = False
            for u in self.users:
                if u.logged == True and u.admin == True:
                    canChange = True
                    break
            if canChange == True:
                os.system('cls')
                print("Increase or decrease payout: \n")
                ok = False
                found = False
                name = str(input("Name: "))
                surname = str(input("Surname: "))
                index = 0
                for u in self.users:
                    if u.name == name and u.surname == surname:
                        found = True
                        print("{} {} - current payout: {}".format(u.name, u.surname, u.payout))
                        choices = ""
                        print("Insert '1' to add to/take from payout value\nInsert '2' to multipy payout value "
                              "(eg. 1.5, 2)\nInsert '3' to set higher/lower payout value")
                        choices = str(input("Insert '1', '2' or '3': "))
                        if choices == "1" or choices == "2" or choices == "3":
                            ok = True
                        else:
                            print("Wrong value")
                        break
                    else:
                        index += 1
                if found == False:
                    print("User {} {} doesn't exist.".format(name, surname))
                elif ok == True:
                    if choices == "1":
                        self.users[index].payout = self.users[index].payout + float(input("Increase/Decrease(-) payout "
                                                                                          "by: "))
                    elif choices == "2":
                        self.users[index].payout = round(self.users[index].payout*float(input("Increase/Decrease payout x "
                                                                                       "times. x = ")),2)
                    elif choices == "3":
                        self.users[index].payout = float(input("Insert new payout value: "))
                    print("New payout value for {} {} is: {}\n".format(self.users[index].name, self.users[index].surname,
                                                                     self.users[index].payout))
            sleep(5)

        def promoteOrDegradeUser(self):
            canChange = False
            for u in self.users:
                if u.logged == True and u.admin == True:
                    canChange = True
                    break

            if canChange == True:
                os.system('cls')
                print("Promote or degrade user: \n")
                ok = False
                name = str(input("Name: "))
                surname = str(input("Surname: "))
                index = 0
                for u in self.users:
                    if u.name == name and u.surname == surname:
                        ok = True
                        break
                    else:
                        index += 1
                if ok == True:
                    good = False
                    print(self.users[index].position, " ", self.users[index].payout, "\n")
                    print("Available positions: ", self.positions[0], ", ", self.positions[1], ", ", self.positions[2],
                          ", ", self.positions[3], ", ", self.positions[4], ", ", self.positions[5], "-Chief executive "
                                                                                                     "officer")
                    position = str(input("New position: "))
                    indn = 0 # new position index
                    indo = 0 # old position index

                    for p in self.positions:
                        if position == p:
                            good = True
                            break
                        else:
                            indn += 1

                    for p in self.positions:
                        if self.users[index].position == p:
                            break
                        else:
                            indo += 1

                    if good == True:
                        self.users[index].position = position
                        self.users[index].payout = self.payouts[indn]
                        if indn > indo:
                            pd="promoted"
                        elif indn == indo:
                            pd="nothing"
                        else:
                            pd="degraded"
                        if pd != "nothing":
                            print("User {} {} got {} from {} to {}. His/her payout is now {}"
                                  "\n".format(name, surname, pd, self.positions[indo], self.users[index].position,
                                              self.users[index].payout))
                        else:
                            print("Nothing happened\n")
                    else:
                        print("Wrong position name\n")
                    sleep(5)

        def giveTask(self):
            os.system('cls')
            canChange = False
            for u in self.users:
                if u.logged == True and u.position != "Employee":
                    pos = u.position
                    canChange = True
                    break
            if canChange == True:
                ok = False
                indexp = 0
                for p in self.positions:
                    if pos == p:
                        break
                    else:
                        indexp += 1
                loe = []#'list of employees' which currently logged user can give tasks to
                for e in self.users:
                    indp = 0
                    for p in self.positions:
                        if p == e.position:
                            break
                        else:
                            indp+=1
                    if indexp > indp:
                        loe.append(e)
                for e in range(len(loe)):
                    print(e+1, ". ", loe[e].name, " ", loe[e].surname, "\n")
                number = int(input("Insert number(INTEGER): "))
                if number > 0 and number <= len(loe):
                    text = "Task for {} {}: ".format(loe[number-1].name, loe[number-1].surname)
                    loe[number-1].task = str(input(text))
                    print("Task assigned to {} {}".format(loe[number-1].name, loe[number-1].surname))
                else:
                    print("Wrong value")
                sleep(5)

        def viewYourTask(self):
            os.system('cls')
            view = False
            index = 0
            for u in self.users:
                if u.logged == True:
                    view = True
                    break
                else:
                    index+=1
            if view == True:
                if self.users[index].task is not None:
                    print("Your task: ", self.users[index].task)
                else:
                    print("You don't have any task assigned\n")
                sleep(7)

        def writeAReport(self):
            os.system('cls')
            index = 0
            view = False
            for u in self.users:
                if u.logged == True:
                    view = True
                    break
                else:
                    index += 1
            if view == True:
                #if self.users[index].report is None:
                print("Your task: \n", self.users[index].task, "\n")
                self.users[index].report = str(input("Your report: "))

        def sendReportToCheck(self):
            view = False
            index = 0
            os.system('cls')
            for u in self.users:
                if u.logged == True:
                    view = True
                    break
                else:
                    index += 1
            if view == True:
                if self.users[index].task is not None:
                    print("Your task: \n", self.users[index].task, "\nYour report: \n", self.users[index].report)
                    confirm = str(input("Are you sure you want to send your task to check?('yes' or 'no'): "))
                    if confirm == "yes":
                        self.users[0].taskToCheck.append(self.users[index].task)
                        self.users[0].usersWhoSentTask.append(self.users[index])
                        self.users[0].receivedTask = 1
                        print("Task has been sent to check")
                    elif confirm == "no":
                        print("Task has not been sent")
                    else:
                        print("Wrong value")
                else:
                    print("You do not have any task to send")

        def checkTasks(self): #only boss
            view = False
            dontGo = False
            os.system('cls')
            for u in self.users:
                if u.logged == True:
                    view = True
                    break
            if view == True:
                if self.users[0].receivedTask is not None:
                    self.users[0].receivedTask = None
                if len(self.users[0].taskToCheck) == 0:
                    print("No one has sent their task to check\n")
                    dontGo = True
                for u in range(len(self.users[0].taskToCheck)):
                    print("{}. {} {}: {}".format(u+1, self.users[0].usersWhoSentTask[u].name,
                                                 self.users[0].usersWhoSentTask[u].surname,
                                                 self.users[0].taskToCheck[u]))
            if dontGo == False:
                choiceU = int(input("Choose user(INTEGER) whose task you want to check: "))
                ok = False
                for i in range(len(self.users[0].taskToCheck)):
                    if choiceU == i+1:
                        ok=True
                        break
                if ok == True:
                    print("Task: ", self.users[0].taskToCheck[choiceU-1], "\nReport: \n", self.users[0].usersWhoSentTask[choiceU-1].report)
                    good = str(input("Is it good?('yes' or 'no'): "))
                    if good == "yes":
                        self.users[0].usersWhoSentTask[choiceU - 1].task = None
                        self.users[0].usersWhoSentTask.remove(self.users[0].usersWhoSentTask[choiceU-1])
                        self.users[0].taskToCheck.remove(self.users[0].taskToCheck[choiceU-1])
                        print("done\n")
                    elif good == "no":
                        print("What's wrong: ")
                        message = "Comment: " + str(input())
                        self.users[0].usersWhoSentTask[choiceU - 1].task = self.users[0].taskToCheck[choiceU - 1] + "\n" + message
                        self.users[0].usersWhoSentTask.remove(self.users[0].usersWhoSentTask[choiceU - 1])
                        self.users[0].taskToCheck.remove(self.users[0].taskToCheck[choiceU - 1])
                    else:
                        print("Wrong value")
                else:
                    print("Wrong value\n")

        def deleteUser(self):
            os.system('cls')
            canChange = False
            for u in self.users:
                if u.logged == True and u.admin == True:
                    canChange = True
                    break

            if canChange == True:
                ok = False
                print("Fire user: \n")
                name = str(input("Name: "))
                surname = str(input("Surname: "))
                index = 0
                for u in self.users:
                    if u.name == name and u.surname == surname:
                        ok = True
                        break
                    else:
                        index+=1
                if ok == True:
                    #self.users.remove(self.users[index])
                    self.users[index].firedNotif = True
                    if self.users[index] in self.users[0].usersWhoSentTask:
                        self.users[0].usersWhoSentTask.remove(self.users[index])
                        self.users[0].taskToCheck.remove(self.users[index].task)
                        #self.users[0].firedUsers.append(self.users[index])
                    print("User {} {} has been fired\n".format(name, surname))
                else:
                    print("User {} {} has not been found\n".format(name, surname))

        def signIn(self):
            os.system('cls')
            print("Sign in:\n")
            success = False
            login = str(input("Login: "))
            password = str(input("Password: "))
            if len(self.users) > 0:
                index =0
                for u in self.users:
                    if u.login == login:
                        if u.password == password:
                            u.logged = True
                            success = True
                            break
                for u in self.users:
                    if u.logged == True:
                        break
                    else:
                        index+=1

                if index < len(self.users):
                    if self.users[index].firedNotif is not None:
                        print("YOU ARE FIRED!!!")
                        self.users.remove(self.users[index])

                    elif success != True:
                        print("Incorrect login or password\n")
                    else:
                        print("Logged in")
                        if self.users[index].task is not None:
                            print("You have a task to do\n")
                        if self.users[index].receivedTask is not None: #only boss
                            print("You have new task to check\n")
                        self.forSignedIn()
                else:
                    print("Incorrect login or password\n")

        def signOut(self):
            success = False
            for u in self.users:
                if u.logged == True:
                    success = True
                    break
            if success == True:
                u.logged = False
                print("Logged out\n")
                sleep(3)

        def forSignedIn(self):
            operationsFor = None
            run = True
            while run:
                for u in self.users:
                    if u.logged == True:
                        sleep(5)
                        os.system('cls')
                        if u.position == "CEO":
                            operationsFor = "CEO"
                            break
                        elif u.position == "Admin":
                            operationsFor = "Admin"
                            break
                        else:
                            operationsFor = "Employee"
                            break
                if operationsFor == "CEO":
                    print("Insert '1' to add user(if company exists)\nInsert '2' to set/change Login and Password(if user "
                          "exists)\nInsert '3' to increase/decrease payout\nInsert '4' to delete user\nInsert '5' to "
                          "promote/degrade user\nInsert '6' to assign task for user\nInsert '7' to check tasks sent by "
                          "users\nInsert '8' to sign out\n")

                    choice = str(input("Choose operation: "))
                    if choice == "1":
                        self.addUser()
                    elif choice == "2":
                        self.setLoginAndPassword()
                    elif choice == "3":
                        self.increaseOrDecreasePayout()
                    elif choice == "4":
                        self.deleteUser()
                    elif choice == "5":
                        self.promoteOrDegradeUser()
                    elif choice == "6":
                        self.giveTask()
                    elif choice == "7":
                        self.checkTasks()
                    elif choice == "8":
                        self.signOut()
                        run = False
                    else:
                        print("Unknown operation. Try again\n")

                elif operationsFor == "Admin":
                    print("Work in progress\n")

                elif operationsFor == "Employee":
                    print("Insert '1' to view your task\nInsert '2' to write a report\nInsert '3' to send your report "
                          "to check\nInsert '4' to sign out\n")

                    choice = str(input("Choose operation: "))
                    if choice == "1":
                        self.viewYourTask()
                    elif choice == "2":
                        self.writeAReport()
                    elif choice == "3":
                        self.sendReportToCheck()
                    elif choice == "4":
                        self.signOut()
                        run = False
                    else:
                        print("Unknown operation. Try again\n")

    """s = company("IT")
    s.users.append(user("root", "", True))
    s.users[0].login = "root"
    s.users[0].password = "root"
    s.signIn()
    s.addUser()
    s.setLoginAndPassword()
    s.signOut()
    s.signIn()
    s.addUser()
    s.signOut()"""

    def programFunctions():
        """
        - uruchomienie programu: włącz program/zatrzymaj \/
        - włącz program: stwóż firmę/zaloguj się/wyłącz program
        - zaloguj się: CEO, admin, pracownik
        - CEO: dodaj użytkownika, ustaw login i hasło, zwiększ/zmniejsz wypłatę, awansuj/degraduj pracownika,
        usuń użytkownika, dodaj zadanie pracownikowi, sprawdź zadania wysłane przez pracowników, wyloguj się
        - admin:
        - pracownik: zobacz swoje zadania, napisz raport, wyślij zadanie/raport do sprawdzenia, wyloguj się
        """
        run = True
        while run:
            os.system('cls')
            print("Insert '1' to create a company(and root)\nInsert '2' to sign in\nInsert '3' to go to main menu\n")
            choice = str(input("Choose operation: "))
            error = False

            if choice == "1":
                os.system('cls')
                name = str(input("Company name: "))
                for i in companies:
                    if i.companyName == name:
                        print("ERROR: Cannot create new company. Company with this name already exists")
                        error = True
                        sleep(3)
                        os.system('cls')
                        break
                if error == False:
                    companies.append(company(name))
                    print("Created '{}' company".format(name))
                    print("Create 'root' user:\n")
                    index = 0
                    for i in companies:
                        if i.companyName == name:
                            break
                        else:
                            index += 1
                    companies[index].users.append(user("root", "", True))
                    companies[index].users[0].position = "CEO"
                    companies[index].users[0].payout = 48000
                    companies[index].users[0].login = str(input("Login for 'root' user: "))
                    companies[index].users[0].password = str(input("Password for 'root' user: "))
                    os.system('cls')
                    print("'Root' user created")
                    sleep(3)
                    os.system('cls')

            elif choice == "2":
                os.system('cls')
                for i in range(len(companies)):
                    print(i + 1, ". ", companies[i].companyName)
                name = str(input("Choose the company(name): "))
                found = False
                for i in companies:
                    if i.companyName == name:
                        found = True
                        i.signIn()
                if found == False:
                    print("Incorrect company name")
                    sleep(3)
                    os.system('cls')

            elif choice == "3":
                os.system('cls')
                run = False

            else:
                print("Unknown operation. Try again\n")
                sleep(3)
                os.system('cls')

            """print("Insert '1' to create a company(and root)\nInsert '2' to sign in\nInsert '3' to add user(if company"
                  " exists)\nInsert '4' to set/change Login and Password(if user exists)\nInsert '5' to "
                  "increase/decrease payout\nInsert '6' to delete user\nInsert '7' to promote/degrade user\nInsert '8' "
                  "to assign task for user\nInsert '10' to view your task\nInsert '11' to write a report\nInsert '12' "
                  "to send your report to check\nInsert '13' to check tasks sent by users\nInsert '9' to sign out\n"
                  "Insert '0' to go to main menu")
            choice = str(input("Choose operation: "))
            error = False
            if choice == "1":
                os.system('cls')
                name = str(input("Company name: "))
                for i in companies:
                    if i.companyName == name:
                        print("ERROR: Cannot create new company. Company with this name already exists")
                        error = True
                        break
                if error == False:
                    companies.append(company(name))
                    print("Created '{}' company".format(name))
                    print("Create 'root' user\n")
                    index = 0
                    for i in companies:
                        if i.companyName == name:
                            break
                        else:
                            index+=1
                    companies[index].users.append(user("root", "", True))
                    companies[index].users[0].position = "CEO"
                    companies[index].users[0].payout = 48000
                    companies[index].users[0].login = str(input("Login for 'root' user: "))
                    companies[index].users[0].password = str(input("Password for 'root' user: "))
                    print("'Root' user created")

            elif choice == "2":
                for i in range(len(companies)):
                    print(i+1, ". ", companies[i].companyName)
                name = str(input("Choose the company(name): "))
                found = False
                for i in companies:
                    if i.companyName == name:
                        found = True
                        i.signIn()
                if found == False:
                    print("Incorrect company name")

            elif choice == "3":
                for i in companies:
                    i.addUser()

            elif choice == "4":
                for i in companies:
                    i.setLoginAndPassword()

            elif choice == "5":
                for i in companies:
                    i.increaseOrDecreasePayout()

            elif choice == "6":
                for i in companies:
                    i.deleteUser()

            elif choice == "7":
                for i in companies:
                    i.promoteOrDegradeUser()

            elif choice == "8":
                for i in companies:
                    i.giveTask()

            elif choice == "10":
                for i in companies:
                    i.viewYourTask()

            elif choice == "11":
                for i in companies:
                    i.writeAReport()

            elif choice == "12":
                for i in companies:
                    i.sendReportToCheck()

            elif choice == "13":
                for i in companies:
                    i.checkTasks()

            elif choice == "9":
                for i in companies:
                    for u in i.users:
                        if u.logged == True:
                            i.signOut()

            elif choice == "0":
                for i in companies:
                    for u in i.users:
                        if u.logged == True:
                            i.signOut()
                            run = False

            else:
                print("Unknown operation. Try again\n")"""

    def system():
        run = True
        while run:
            choice = str(input("Insert '1' to open program\nInsert '0' to close program: "))
            if choice != "1" and choice != "0":
                print("Unknown operation. Try again\n")
            elif choice == "0":
                countdown = 5
                print("Closing program in:")
                for i in range(countdown):
                    print(countdown)
                    countdown = countdown - 1
                    sleep(1)
                run = False
            elif choice == "1":
                programFunctions()

    system()


if __name__ == "__main__":
    main()
