print("1:Hello there? ")
print("2:This programme was made aimimng to understand python basics.")
print("____________________________________________________________________")
print("1. simple interest.")
print("2. compound interest.")
print("3. quadratic equation.")
print("4. Riddle Game.")
print("_____________________________________________________________________")
choice = input("input choice from above: ")

if choice == "1":
    print("________________________________________________________________")
    print(" ____              ___          ___                             ")
    print(" |___  |  |\\  /|  |___|  |      |__                            ")
    print(" ____| |  | \\/ |  |      |___   |__                            ")
    print("                  |                                             ")
    print("  ___         _____ ___  ___  ___  ___  ___                     ")
    print("   |    |\\ |    |   |__  |__| |__  |__   |                     ")
    print("  _|_   | \\|    |   |__  | \\  |__  ___|  |           by Brian.")
    print("________________________________________________________________")

    print("you chose simple interest: ")

    deposit = input("input the deposit here: ")
    rate = input("input the interest rate here: ")
    time = input("input the time in years here: ")
    result = float(deposit) * float(rate) * float(time) / 100
    print("")
    print("")
    print("The simple interest is:  "+ str(float(result)))
    print("")
    print("_______________________________________________________________________")
# This prints the results of simple interest alone excluding the initial deposit    print("______________________________________________________________________")

if choice =="2":
    print("________________________________________________________________")
    print("   ___    __          ___   __                                  ")
    print("   |     |  |  |\\  /| |__| |  |   |  |  |\\ |  |\\             ")
    print("   |__   |__|  | \\/ | |    |__|   |__|  | \\|  |_|             ")
    print("                                                                ")
    print("   ___       ___  ___   ___  ___  ___  ___                      ")
    print("    |   |\\ |  |   |__   |__| |__  |__   |                      ")
    print("   _|_  | \\|  |   |__   | \\  |__  ___|  |            by Brian.")
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
    discriminant = b**2 - 4*a*c
    result1 = (-b + math.sqrt(discriminant)) / (2*a)
    result2 = (-b - math.sqrt(discriminant)) / (2*a)

    print("the formulae = ax^2 + bx + c")
    print("therefore we substitute a b and c")
    print("________________________________________________________")
    print("this becomes " + str(a)+" x^2 + " + str(b) + " x " + str(c))
    print("")
    print("the quadratic equation is {-b ± √b -4ac /2a}")
    print("")
    print("therefore the substitution becomes"+ str(-b) + " ± " + str(b) + " - " + str(4*a*c) + " / " + str(2*a))
    print("")
    print("")
    print(" x is therefore equal to:" + str(result1) + " or " + str(result2))
    print("_________________________________________________________")
    print("thanks for using this programme.")
    print("_________________________________________________________")
if choice == "4":
    print("RIDDLE GAME! ")
    secret_word = "egg"
    guess = ""
    while guess != secret_word:
        guess = input("my house has no doors: ")
    print("well done you got it!    its an egg")

    print("_________________________________________________________")
    print("next riddle: ")
    next_secret_word = "tortoise"
    guess = ""
    while guess != next_secret_word:
        guess = input("am slow as f*ck: ")
    print("well done you got it!    its a tortoise!!")


    print("Well done you have found an easter egg!: ")
    next_secret_word = "egg"
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False
    while guess != next_secret_word:

        if guess_count < guess_limit:
            guess = input("input password to get source code, you have 3 attempts!: ")
            guess_count += 1
        else:
          out_of_guesses = True

    if out_of_guesses:
     print("sorry better luck next time bro: ")
    else :
     print("nice here you go: ")
     print("bruuhhhhhhhhh(ssds)sd90s)(((((ds0d9s09ds09d09s09d09s09d09s0n()SJDNJSKBKJDBJKJ  happy now")



if choice == "29":
    print("Well done you just found my favorite number, you are deemed worthy of taking on my project"
          "here is the source code my brethren:")

