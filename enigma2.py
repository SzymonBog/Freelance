from randomNumbersGenerator import randint


letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A",
          "B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ",",",
          ".","/","<",">","?",";",":","{","}","[","]","|","0","1","2","3","4","5","6","7","8","9","`","~","!","@","#",
          "$","%","^","&","*","(",")","_","+","-","="]
decipher = [94]*92
indexes = [94]*92
currentIndex = 0
number = 0
index = 0

cipher = []

while number < 92:
    currentIndex = randint(0, 91)
    if indexes.__contains__(currentIndex) == False:
        indexes[index] = currentIndex
        decipher[index] = letters[currentIndex]
        number+=1
        """for i in indexes:
            index2 = 0
            for j in letters:
                if i < 91:
                    if letters[i] == j:
                        break
                    else:
                        index2 += 1
            if index2 < 92:
                indexes[index2] = index2
                decipher[91-index2] = letters[index2]"""
        index+=1

print("Enigma2")


def encode():
    """
    for i in range(len(letters)):
            print(letters[i], " - ", decipher[i])
    """
    message = str(input("Wiadomość do zakodowania: "))
    encodedMessage = ""

    for e in message:
        currentIndex = 0
        for k in letters:
            if e == k:
                encodedMessage = encodedMessage + decipher[currentIndex]
                break
            else:
                currentIndex += 1

    print(encodedMessage)
    return encodedMessage


def decode(encodedMessage=""):
    #encodedMessage = str(input("Encoded message: "))
    message = ""
    for l in encodedMessage:
        currentIndex =0
        for k in decipher:
            if l == k:
                message = message + letters[currentIndex]
                break
            else:
                currentIndex +=1

    print(message)


run = True
while run:
    print("Insert '1' to encode your message\nInsert '2' to decode a message\nInsert '0' to exit\n")
    chioce = str(input("Choice: \n"))
    if chioce == "1":
        cipher.append(encode())
    elif chioce == "2":
        if len(cipher) != 0:
            print("Choose: ")
            for i in range(len(cipher)):
                print("{}. {}".format(i+1,cipher[i]))
            choice2 = int(input("Choice2: \n"))
            if choice2 > len(cipher) or choice2 < 0:
                print("Wrong number\n")
            else:
                decode(cipher[choice2-1])
        else:
            print("There is no cipher to decode\n")
    elif chioce == "0":
        exit(0)
    else:
        print("Unknown command. Try again.\n")
