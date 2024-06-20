import randomNumbersGenerator
import random


"""
This simple program can generate binary file content. I use this to try to recreate the game 'hacknet'
"""

# 75
while True:
    i = input("Length(how many bits): ")
    try:
        i = int(i)
        if i <= 0:
            print("Length has to be greater than 0")
        else:
            #
            ind = 75
            #
            s = ""
            for j in range(i):
                #
                if j == ind:
                    s += "\\n"
                    ind += 75
                #
                s += str(random.randint(0, 1))
            print(s)
    except ValueError:
        if i == "quit" or i == "exit":
            quit(666)
            # quit('666')  # it prints red 666 XD
        print("You cannot do this. If you want to quit, type: 'quit' or 'exit'")
