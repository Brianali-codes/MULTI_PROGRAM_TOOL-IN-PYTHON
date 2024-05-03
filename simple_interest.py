
print("Hello there? ")
print("This programme was made aiming to understand python basics.")
print("____________________________________________________________________")
print("1. simple interest.")
print("2. compound interest.")
print("3. quadratic equation.")
print("4. Riddle Game.")
print("5. Password guessing game")
print("6. simple calculator")
print("_____________________________________________________________________")
choice = input("input choice from above: ")


def simple_interest():
    # program for calculating simple interest.
    print("________________________________________________________________")
    print("you chose simple interest: ")
    # asks user to input different values related to their simple interest calculation
    deposit = input("input the deposit here: ")
    rate = input("input the interest rate here: ")
    time = input("input the time in years here: ")
    result = float(deposit) * float(rate) * float(time) / 100
    print("")
    print("")
    print("The simple interest is: " + str(float(result)))
    print("")
    print("")
    print("_______________________________________________________________________")
    # This prints the results of simple interest alone excluding the initial deposit
    print("______________________________________________________________________")


def compound_interest():
    # program for calculating compound interest.
    print("________________________________________________________________")
    print("you chose compound interest: ")
    # asks for compound interest input values from the user.
    deposit = float(input("input the deposit here: "))
    rate = float(input("input the interest rate in percentage here: "))
    time = float(input("input the time in years here: "))
    result = deposit * ((1 + rate / 100) ** time - 1)
    print("")

    # This prints the results of compound interest alone excluding the initial deposit
    print("The compound interest is: " + str(float(result)))
    print("")
    print("thanks for using my programme.")
    print("______________________________________________________________________")


def quadratic_equations():
    # program for calculating quadratic equations.
    import math

    print("simple quadratic equations programme")
    a = float(input("input a here:"))
    b = float(input("input b here:"))
    c = float(input("input c here:"))
    # Input coefficients.
    discriminant = b ** 2 - 4 * a * c
    result1 = (-b + math.sqrt(discriminant)) / (2 * a)
    result2 = (-b - math.sqrt(discriminant)) / (2 * a)
    # calculates discriminants.
    print("_______________________________________________________________")
    print("the formulae = ax^2 + bx + c")
    print("therefore we substitute a b and c")
    print("_______________________________________________________________")
    print("this becomes " + str(a) + " x^2 + " + str(b) + " x " + "+" + str(c))
    print("")
    print("the quadratic equation is {-b ± √b -4ac /2a}")
    print("")
    print("therefore the substitution becomes " + str(-b) + " ± " + str(b) + "-" + str(4 * a * c) + " / " + str(2 * a))
    print("")
    print("")
    print(" x is therefore equal to:" + str(round(result1, 2)) + " or " + str(round(result2, 2)))
    print("________________________________________________________________")
    print("thanks for using this programme.")
    print("________________________________________________________________")


def riddle_game():
    # program for a riddle game.
    print("RIDDLE GAME! ")
    # the user has to guess correctly in order to match the secret word to the guess.
    print("the riddle game consists of 10 riddles the programme may not\n be entirely accurate.")
    print("riddle 1: ")
    secret_word = "feather"
    guess = ""
    while guess != secret_word:
        guess = input("I am easy to lift, but hard to throw. What am I?: ")
        print("try again")
    print("well done you got it! its a feather. ")

    print("_________________________________________________________")
    print("")
    print("2nd riddle: ")
    next_secret_word = "river"
    guess = ""
    while guess != next_secret_word:
        guess = input("What can run but never walk"
                      "\nhas a head but never weeps, "
                      "\nhas a bed but. never sleeps?: ")
        print("try again")
    print("well done you got it! its a river!!")

    print("_________________________________________________________")
    print("third riddle")
    secret_word2 = "age"
    guess = ""
    while guess != secret_word2:
        guess = input("What goes up but never comes down? ")
        print("try again")
    print("well done you got it! its your age. ")

    print("_________________________________________________________")

    print("fourth riddle. ")
    secret_word3 = "footsteps"
    guess = ""
    while guess != secret_word3:
        guess = input("The more you take, the more\n you leave behind. What am I?")
        print("try again")
    print(" well done its your footsteps")

    print("_________________________________________________________")

    print("fifth riddle. ")
    secret_word4 = "piano"
    guess = ""
    while guess != secret_word4:
        guess = input("What has keys but can't open locks?")
        print("try again")
    print(" well done its a piano.")

    print("_________________________________________________________")

    print("sixth riddle. ")
    secret_word5 = "penny"
    guess = ""
    while guess != secret_word5:
        guess = input("What has a head, a tail, is brown, and has no legs?")
        print("try again")
    print(" well done its a penny.")

    print("_________________________________________________________")

    print("seventh riddle. ")
    secret_word6 = "stamp"
    guess = ""
    while guess != secret_word6:
        guess = input("What travels the world while staying on a corner")
        print("try again")
    print(" well done its a stamp.")

    print("_________________________________________________________")

    print("eighth riddle. ")
    secret_word7 = "m"
    guess = ""
    while guess != secret_word7:
        guess = input(" What comes once in a minute, \n"
                      "twice in a moment, but never in a thousand years")
        print("try again")
    print(" well done its the letter m.")

    print("_________________________________________________________")
    print("ninth riddle")
    secret_word8 = "bottle"
    guess = ""
    while guess != secret_word8:
        guess = input("What has a neck but no head?")
        print("try again")
    print(" well done its a bottle.")

    print("_________________________________________________________")

    print("tenth riddle")
    secret_word9 = "time"
    guess = ""
    while guess != secret_word9:
        guess = input("The more you take, the more you leave behind. What am I?")
        print("try again")
    print(" well done its time.")

    # if the user answers wrong then the programme loops and asks to try again.

    print("_________________________________________________________")


def password_guessing_game():
    # program for a password guessing game.
    print("password guess")
    guess1 = "password"
    guess0 = ""
    while guess0 != guess1:
        guess0 = input("input guess:")
        if guess0 != guess1:
            print("wrong!!!")
        else:
            print("correct!!!")


def simple_calculator():
    # program for a simple calculator which takes user input and converts it into variables which are
    # part of the programmes logic
    print("simple calculator")
    num_1 = float(input("Input your first number"))
    operator = input("input operator( x + / or + )")
    num_2 = float(input("Input your second number"))

    results = None

    if operator == "+":
        results = num_1 + num_2
    if operator == "-":
        results = num_1 - num_2
    if operator == "/":
        results = num_1 / num_2
    if operator == "*":
        results = num_1 * num_2
    if operator == '/' and num_2 == 0:
        print("Error! Division by zero.")

    if results is not None:
        print("Result:", results)


if choice == "1":
    simple_interest()
elif choice == "2":
    compound_interest()
elif choice == "3":
    quadratic_equations()
elif choice == "4":
    riddle_game()
elif choice == "5":
    password_guessing_game()
elif choice == "6":
    simple_calculator()
else:
    print("invalid choice choose again.")
