import os


# function for history
def history(fnum, choice, snum,claculation):
    his_file = open("history.txt", "w")
    #his_file.write(str(fnum) + " " + str(choice) + " " + str(snum) + "=" + str(claculation) + "\n")
    his_file.write("{} {} {} = {}".format(str(fnum), str(choice), str(snum), str(claculation)))
    his_file.close()


# functions for calculations
# for adding
def add(x, y):
    return x + y


# for subtraction
def sub(x, y):
    return x - y


# for multiplication
def mul(x, y):
    return x * y


# for division
def divi(x, y):
    return x / y


def power(x, y):
    return pow(x, y)


def rem(x, y):
    return x % y


def input_choice(choice):
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)

    # function for the input the numbers and do the rest


def select_op(choice):
    # when choice == # program should be terminated before get the numbers from the user
    if choice == '#':
        print("Program terminated!!!")
        file = open("history.txt", "r+")
        file. truncate(0)
        file. close()
        exit()

    if choice == '?':
       
        if os.path.getsize('history.txt') == 0:
                print('File is empty')
        else:
            his_file = open("history.txt", "r")
            my_txt = his_file.read()
            print(my_txt)
            #his_file.close()
        return
    if choice == '+' or choice == '-' or choice == '*' or choice == '/' or choice == '^' or choice == '%':
        fnum = input("Enter the first number  : ")
        print(fnum)
        # when type the dolor sign"$" program will return to the main menu
        if fnum[-1] == '$':
            return
        # when we enter hash program will be terminated
        if fnum == '#':
            print("Program terminated!!!")
            exit()

        snum = input("Enter the second number : ")
        print(snum)
        # when type the dolor sign"$" program will return to the main menu
        if snum[-1] == '$':
            return
        # when we enter hash program will be terminated
        if snum == '#':
            print("Program terminated!!!")
            exit()

    else:
        print("Unrecognized operation")
    fnum = float(fnum)
    snum = float(snum)

    # looking
    # while True:
    if choice == '+':
        # a = add(fnum,snum)
        print(fnum, "+", snum, "=", add(fnum, snum))
        history(fnum, choice, snum, add(fnum, snum))

    elif choice == '-':
        print(fnum, "-", snum, "=", sub(fnum, snum))
        history(fnum, choice, snum, sub(fnum, snum))

    elif choice == '*':
        print(fnum, "*", snum, "=", mul(fnum, snum))
        history(fnum, choice, snum, mul(fnum, snum))

    elif choice == '/':
        if snum == 0:
            print("This can not be defined")
        else:
            print(fnum, "/", snum, "=", divi(fnum, snum))
            history(fnum, choice, snum, divi(fnum, snum))

    elif choice == '^':
        print(fnum, "^", snum, "=", power(fnum, snum))
        history(fnum, choice, snum, power(fnum, snum))

    elif choice == '%':
        print(fnum, "%", snum, "=", rem(fnum, snum))
        history(fnum, choice, snum, rem(fnum, snum))

    #elif choice == '?':
     #   his_file = open("history.txt", "r")
      #  my_txt = his_file.read()
       # print(my_txt)


while True:
    print("Select operation.")
    print("1. Add       : + ")
    print("2. Subtract  : - ")
    print("3. Multiply  : * ")
    print("4. Divide    : / ")
    print("5. Power     : ^ ")
    print("6. Remainder : % ")
    print("7. Terminate : # ")
    print("8. Reset     : $ ")
    print("9. History   : ? ")

    # take input

    choice_x = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
    print(choice_x)
    select_op(choice_x)
