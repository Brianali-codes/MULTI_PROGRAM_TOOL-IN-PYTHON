
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

if choice == "1":
    print("________________________________________________________________")
    print("you chose simple interest: ")

    deposit = input("input the deposit here: ")
    rate = input("input the interest rate here: ")
    time = input("input the time in years here: ")
    result = float(deposit) * float(rate) * float(time) / 100
    print("")
    print("")
    print("The simple interest is: " + str(float(result)))
    print("")
    print("_______________________________________________________________________")
    # This prints the results of simple interest alone excluding the initial deposit
    print("______________________________________________________________________")

if choice == "2":
    print("________________________________________________________________")
    print("you chose compound interest: ")

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

if choice == "3":
    import math

    print("simple quadratic equations programme")
    a = float(input("input a here:"))
    b = float(input("input b here:"))
    c = float(input("input c here:"))
    discriminant = b ** 2 - 4 * a * c
    result1 = (-b + math.sqrt(discriminant)) / (2 * a)
    result2 = (-b - math.sqrt(discriminant)) / (2 * a)
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
    print(" x is therefore equal to:" + str(result1) + " or " + str(result2))
    print("________________________________________________________________")
    print("thanks for using this programme.")
    print("________________________________________________________________")
if choice == "4":
    print("RIDDLE GAME! ")
    secret_word = "feather"
    guess = ""
    while guess != secret_word:
        guess = input("I am easy to lift, but hard to throw. What am I?: ")
        print("try again")
    print("well done you got it! its a feather. ")

    print("_________________________________________________________")
    print("2nd riddle: ")
    next_secret_word = "river"
    guess = ""
    while guess != next_secret_word:
        guess = input("What can run but never walk"
                      "\nhas a head but never weeps, "
                      "\nhas a bed but. never sleeps?: ")
        print("try again")
    print("well done you got it! its a river!!")
    print("third riddle")
    secret_word2 = "age"
    guess = ""
    while guess != secret_word2:
        guess = input("What goes up but never comes down? ")
        print("try again")
    print("well done you got it! its your age. ")

if choice == "29":
    print("Well done you just found my favorite number, "
          "you are deemed worthy"
          " of taking on my project"
          "here is the source code my brethren:")
if choice == "5":
    print("password guess")
    guess1 = "password"
    guess0 = ""
    while guess0 != guess1:
        guess0 = input("input guess:")
        if guess0 != guess1:
            print("wrong!!!")
        else:
            print("correct!!!")
if choice == "6":
    print("simple calculator")
    num_1 = float(input("Input your first number"))
    operator = input("input operator( x + / or + )")
    num_2 = float(input("Input your first number"))
    result4 = int(num_1)+int(operator)+int(num_2)

    print(result4)
