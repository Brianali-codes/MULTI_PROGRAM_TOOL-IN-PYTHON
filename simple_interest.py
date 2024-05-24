import random


def main():
    def start_programme():
        print("Hello there? ")
        print("This programme was made aiming to understand python basics.")
        print("____________________________________________________________________")
        print("1. simple interest.")
        print("2. compound interest.")
        print("3. quadratic equation.")
        print("4. Riddle Game.")
        print("5. Password guessr.")
        print("6. simple calculator")
        print("7. power calculator.")
        print("8. True or false.")
        print("9. rock paper scissors.")
        print("10.random recipe generator.")
        print("_____________________________________________________________________")

    start_programme()

    def simple_interest():
        # program for calculating simple interest.
        print("________________________________________________________________")
        print("you chose simple interest: ")
        # asks user to input different values related to their simple interest calculation
        deposit = input("input the deposit here: ")
        rate = input("input the interest rate here: ")
        time = input("input the time in years here: ")
        result = float(deposit) * float(rate) * float(time) / 100
        # round to 3 decimal places in order to make the answer better presented.
        final_result = round(result, 3)
        print("")
        print("")
        print("The simple interest is: " + str(float(final_result)))
        print("")
        print("")
        print("_______________________________________________________________________")
        # This prints the results of simple interest alone excluding the initial deposit
        print("______________________________________________________________________")
        # prompts the user to restart the programme.
        # programme also restarts anyway no matter the input
        # this sections is to reduce amount of output on the screen
        choices_1 = ["1", "2"]
        input_1 = ""
        while input_1 not in choices_1:
            input_1 = input("input 1 to restart or 2 for simple interest again.: ")
            if input_1 == "1":
                main()
            elif input_1 == "2":
                simple_interest()

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
        print("________________________________________________________________")
        input_2 = ""
        choices_2 = ["1," "2"]
        while input_2 not in choices_2:
            input_2 = input(str("input 1 to go back or 2 to restart compound interest!: "))
            if input_2 == "1":
                main()
            elif input_2 == "2":
                compound_interest()

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
        print("the formulae is: ax^2 + bx + c = 0.")
        print("therefore we substitute a b and c")
        print("_______________________________________________________________")
        print("this becomes " + str(a) + " x^2 + " + str(b) + " x " + "+" + str(c))
        print("")
        print("the quadratic equation is {-b ± √b -4ac /2a}")
        print("")
        print("therefore the substitution becomes " + str(-b) + " ± " + str(b) + "-" + str(4 * a * c) + " / " + str(
            2 * a))
        print("")
        print("")
        print(" x is therefore equal to:" + str(round(result1, 3)) + " or " + str(round(result2, 3)))
        print("________________________________________________________________")
        print("thanks for using this programme.")
        print("________________________________________________________________")
        choices_3 = ["1", "2"]
        input_3 = ""
        while input_3 not in choices_3:
            input_3 = input("input 1 to restart or 2 for quadratic equations: ")
            if input_3 == "1":
                main()
            else:
                quadratic_equations()

    def riddle_game():
        answers = ["feather", "river", "age", "footsteps", "piano", "penny", "stamp", "m", "bottle", "time"]
        # program for a riddle game.
        print("RIDDLE GAME! ")
        # the user has to guess correctly in order to match the secret word to the guess.
        print("the riddle game consists of 10 riddles the programme may not\n be entirely accurate.")
        print("riddle 1: ")
        score = 0
        guess = input("I am easy to lift, but hard to throw. What am I?: ").lower()
        if guess != answers[0]:
            print("wrong")
        else:
            score += 1
            print("well done you got it! its a feather. ")

        print("_________________________________________________________")
        print("")
        print("2nd riddle: ")
        guess = input("i have a head but can not drink, a tail but cant swim\n"
                      "what am i?")
        if guess != answers[1]:
            print("wrong")
        else:
            score += 1
            print("well done you got it! its a river. ")
        print("_________________________________________________________")
        print("third riddle")
        guess = ""
        guess = input("What goes up but never comes down?: ").lower()
        if guess != answers[2]:
            print("wrong!")
        else:
            score += 1
            print("well done you got it! its your age.")
        print("_________________________________________________________")

        print("fourth riddle. ")
        guess = input("The more you take, the more\n you leave behind. What am I?: ").lower()
        print(" well done its your footsteps")
        if guess != answers[3]:
            print("wrong!!!")
        else:
            score += 1
            print(" well done its your footsteps")
        print("_________________________________________________________")

        print("fifth riddle. ")
        guess = input("What has keys but can't open locks?: ").lower()

        if guess != answers[4]:
            print("wrong")
        else:
            score += 1
            print(" well done its a piano.")
        print("_________________________________________________________")

        print("sixth riddle. ")
        guess = input("What has a head, a tail, is brown, and has no legs?: ").lower()

        if guess != answers[5]:
            print("wrong!!!")
        else:
            score += 1
            print(" well done its a penny.")

        print("_________________________________________________________")

        print("seventh riddle. ")
        guess = input("What travels the world while staying on a corner?: ").lower()

        if guess != answers[6]:
            print("wrong")
        else:
            score += 1
            print(" well done its a stamp.")

        print("_________________________________________________________")

        print("eighth riddle. ")
        guess = input(" What comes once in a minute, \n"
                      "twice in a moment, but never in a thousand years: ").lower()

        if guess != answers[7]:
            print("wrong")
        else:
            score += 1
            print(" well done its the letter m.")

        print("_________________________________________________________")

        print("ninth riddle")
        guess = input("What has a neck but no head?: ").lower()
        if guess != answers[8]:
            print("wrong!!!")
        else:
            score += 1
            print(" well done its a bottle.")

        print("_________________________________________________________")

        print("tenth riddle")
        guess = input("The more you take, the more you leave behind. What am I?: ").lower()
        if guess != answers[9]:
            print("wrong")
        else:
            score += 1
            print("well done its time.")
        print("")
        # this section records the score and gives the appropriate pep talk :)
        if score < 6:
            print("come on you can do better, you got " + str(score) + " / 10!")
        else:
            print("congratulations you got " + str(score) + "/ 10.")
        print("")
        input_1 = input("input 1 to restart or 2 to replay(riddle game): ")
        if input_1 == "1":
            main()
        else:
            print("ok ill restart it anyways :)")
            riddle_game()

        # if the user answers wrong the score is 0 and when right score adds 1.

        print("_________________________________________________________")

    def password_guessing_game():
        # program for a password guessing game.
        print("password guess")
        guess1 = "password"
        guess0 = ""
        guesses = 0
        total_guesses = 6
        while guess0 != guess1:

            guesses += 1
            if guesses < total_guesses != guess1:
                guess0 = input("input guess you have 5 attempts:")
            else:
                print("blocked!!!")
                break
            if guess0 == guess1:
                print("correct!")
            else:
                print("wrong!!!")

        input_1 = input("input 1 to restart the programme or 2 for a rerun.: ")
        if input_1 == "1":
            main()
        else:
            print("ok ill restart it anyways :)")
            password_guessing_game()

    def simple_calculator():
        # program for a simple calculator which takes user input and converts it into variables which are
        # part of the programmes logic
        print("simple calculator")
        print("this is a simple calculator therefore it can only \n"
              "do simple tasks negatives and squares are not yet supported.")
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
            return

        if results is not None:
            print("_______________________________________________")
            print("Result:", results)
        else:
            print("invalid operator or choice")
        input_1 = input("input 1 to restart or 2 to relaunch calculator: ")
        if input_1 == "1":
            main()
        else:
            print("ok ill restart it anyways :)")
            simple_calculator()

    def power_calculator():
        print("power calculator: ")
        num_1 = float(input("input your First number: "))
        num_2 = float(input("input power: "))
        result5 = num_1 ** num_2
        print("________________________________________________")
        result6 = result5 / 100000000000000000000000
        if result5 > 10000000000000000000000:
            print(result6)
            print("result is large what are you doing with this: LOL")
            print("Anyways the result to a power variation is:  ", result6, " * 10 ^ 9 ", )
        else:
            print("The answer is: " + str(result5))
        input_1 = input("input 1 to restart: ")
        if input_1 == "1":
            main()
        else:
            print("ok ill restart it anyways :)")
            main()

    def true_or_false():
        print("____________________________________________________________")
        print("This is a true and false game.")
        print("you are only allowed to answer one of two choices true or false")
        print("____________________________________________________________")
        # stat means statement.
        # stat 1 store key input which should be same as user guess in order to
        # complete the loops
        stat1 = "true"
        user_guess = ""
        while user_guess != stat1:
            print("1.There are more iterations of a game of chess \n "
                  "than there are atoms in the observable universe. ")
            user_guess = input("input true or false: ").lower()
            if user_guess != stat1:
                print("try again: ")
            else:
                print("______________________________________________")
                print("nice there are actually more than you think.")
                print("_______________________________________________")
        input_1 = input("input 1 to restart: ")
        if input_1 == "1":
            main()
        else:
            print("ok ill restart it anyways :)")
            main()

    def rock_paper_scissors():
        # function for the rock paper scissors game.

        def start_game():
            print("welcome to rock paper scissors")
            comp_choices = ["rock", "paper", "scissors"]
            computer_choice = random.choice(comp_choices)
            user_choice = ""

            while user_choice not in comp_choices:
                user_choice = input("input your choice here: ").lower()

            print("________________________________________________")
            print("you chose ", user_choice)
            print("computer chose", computer_choice)
            print("________________________________________________")

            if (user_choice == "rock" and computer_choice == "paper"
                    or user_choice == "paper" and computer_choice == "scissors"
                    or user_choice == "scissors" and computer_choice == "rock"):
                print("computer wins!")
            else:
                print("you win!")

            if user_choice == computer_choice:
                print("its a tie")
            play_again = input("do you wanna play again? Y for yes & N for no: ").lower()

            if play_again == "Y":
                start_game()
            else:
                main()

        start_game()

    def random_recipe_generator():
        print("Welcome to the random recipe generator")
        recipe_list = ["Balsamic Glazed Salmon: \n"
                       ""
                       "Ingredients:\n"
                       ""
                       "4 salmon fillets\n"
                       "1/4 cup balsamic vinegar\n"
                       "2 tablespoons honey\n"
                       "2 cloves garlic, minced\n"
                       "Salt and pepper to taste\n"
                       "Fresh herbs for garnish (optional)\n"
                       ""
                       "Instructions:\n"
                       ""
                       "Preheat your oven to 400°F (200°C) and line a baking sheet with parchment paper.\n"
                       "In a small saucepan, combine balsamic vinegar, honey, and minced garlic. Cook over medium "
                       "heat until the mixture thickens slightly, about 5-7 minutes.\n"
                       "Place the salmon fillets on the prepared baking sheet and season with salt and pepper.\n"
                       "Brush the balsamic glaze over the salmon fillets, reserving some for serving.\n"
                       "Bake in the preheated oven for 12-15 minutes,\n"
                       " or until the salmon is cooked through and flakes easily with a fork.\n"
                       "Serve the salmon hot, drizzled with the remaining balsamic glaze and add herbs to your liking",
                       ""
                       "Caprese Pasta Salad: \n"
                       ""
                       "Ingredients:\n"
                       ""
                       "8 oz (225g) fusilli or penne pasta\n"
                       "1 cup cherry tomatoes, halved\n"
                       "1 cup fresh mozzarella balls, halved\n"
                       "1/4 cup fresh basil leaves, torn\n"
                       "2 tablespoons extra virgin olive oil\n"
                       "2 tablespoons balsamic vinegar\n"
                       "Salt and pepper to taste\n"
                       "Instructions:\n"
                       "Cook the pasta according to package instructions until al dente. "
                       "Drain and rinse under cold water to cool.\n"
                       "In a large bowl, combine the cooked pasta, cherry tomatoes, fresh mozzarella, and torn basil leaves.\n"
                       "In a small bowl, whisk together the extra virgin olive oil and balsamic vinegar.  "
                       "Season with salt and pepper to taste.\n"
                       "Pour the dressing over the pasta salad and toss until everything is evenly coated.\n"
                       "Chill in the refrigerator for at least 30 minutes before serving to allow the flavors to meld together.\n"
                       "Serve cold as a refreshing side dish or light main course.",

                       "Classic Margherita Pizza: \n"
                       ""
                       "Ingredients:\n"
                       ""
                       "1 pizza dough ball (store-bought or homemade)\n"
                       "1/2 cup pizza sauce\n"
                       "8 oz fresh mozzarella cheese, sliced\n"
                       "2 large tomatoes, thinly sliced\n"
                       "Fresh basil leaves\n"
                       "Extra virgin olive oil\n"
                       "Salt and pepper to taste\n"
                       ""
                       "Instructions:\n"
                       ""
                       "Preheat your oven to the highest temperature (usually around 500°F or 260°C).\n"
                       "Roll out the pizza dough on a floured surface to your desired thickness.\n"
                       "Transfer the dough to a pizza stone or baking sheet.\n"
                       "Spread the pizza sauce evenly over the dough, leaving a small border around the edges.\n"
                       "Arrange the sliced mozzarella and tomato slices on top of the sauce.\n"
                       "Drizzle with a little extra virgin olive oil and season with salt and pepper.\n"
                       "Bake in the preheated oven for 10-12 minutes, or until the crust is golden and cheese is bubbly.\n"
                       "Remove from the oven and top with fresh basil leaves before serving.",

                       "Chicken Alfredo Pasta: \n"
                       ""
                       "Ingredients:\n"
                       ""
                       "8 oz fettuccine pasta\n"
                       "2 boneless, skinless chicken breasts, sliced\n"
                       "2 tablespoons butter\n"
                       "2 cloves garlic, minced\n"
                       "1 cup heavy cream\n"
                       "1 cup grated Parmesan cheese\n"
                       "Salt and pepper to taste\n"
                       "Fresh parsley for garnish\n"
                       "Instructions:\n"
                       "Cook the fettuccine pasta according to package instructions until al dente. Drain and set aside.\n"
                       "In a large skillet, melt the butter over medium heat. Add the sliced chicken breasts and cook until browned and cooked through, about 5-6 minutes per side.\n"
                       "Add the minced garlic to the skillet and cook for an additional 1-2 minutes.\n"
                       "Pour in the heavy cream and bring to a simmer. Cook for 2-3 minutes, stirring occasionally.\n"
                       "Stir in the grated Parmesan cheese until melted and smooth.\n"
                       "Season the sauce with salt and pepper to taste.\n"
                       "Add the cooked fettuccine to the skillet and toss to coat in the sauce.\n"
                       "Serve hot, garnished with fresh parsley.",

                       "Vegetable Stir-Fry: \n"
                       ""
                       "Ingredients:\n"
                       ""
                       "2 tablespoons vegetable oil\n"
                       "1 onion, sliced\n"
                       "2 cloves garlic, minced\n"
                       "1 bell pepper, sliced\n"
                       "2 carrots, julienned\n"
                       "1 cup broccoli florets\n"
                       "1 cup snap peas\n"
                       "1/4 cup soy sauce\n"
                       "2 tablespoons oyster sauce\n"
                       "1 tablespoon sesame oil\n"
                       "1 tablespoon cornstarch\n"
                       "Cooked rice, for serving\n"
                       "Instructions:\n"
                       "Heat the vegetable oil in a large skillet or wok over high heat.\n"
                       "Add the sliced onion and minced garlic to the skillet and stir-fry for 1-2 minutes.\n"
                       "Add the bell pepper, carrots, broccoli, and snap peas to the skillet. Stir-fry for an additional 3-4 minutes, or until the vegetables are tender-crisp.\n"
                       "In a small bowl, whisk together the soy sauce, oyster sauce, sesame oil, and cornstarch.\n"
                       "Pour the sauce over the vegetables in the skillet and toss to coat.\n"
                       "Cook for another 1-2 minutes, or until the sauce has thickened.\n"
                       "Serve the vegetable stir-fry hot over cooked rice.",

                       "Homemade Chicken Noodle Soup: \n"
                       ""
                       "Ingredients:\n"
                       ""
                       "2 tablespoons olive oil\n"
                       "1 onion, diced\n"
                       "2 carrots, sliced\n"
                       "2 celery stalks, sliced\n"
                       "2 cloves garlic, minced\n"
                       "8 cups chicken broth\n"
                       "2 cups shredded cooked chicken\n"
                       "2 cups egg noodles\n"
                       "2 bay leaves\n"
                       "1 teaspoon dried thyme\n"
                       "Salt and pepper to taste\n"
                       "Fresh parsley for garnish\n"
                       ""
                       "Instructions:\n"
                       ""
                       "In a large pot, heat the olive oil over medium heat.\n"
                       "Add the diced onion, sliced carrots, and sliced celery to the pot. Cook for 5-6 minutes, or until the vegetables are softened.\n"
                       "Add the minced garlic to the pot and cook for an additional 1-2 minutes.\n"
                       "Pour in the chicken broth and add the shredded cooked chicken, egg noodles, bay leaves, and dried thyme.\n"
                       "Bring the soup to a simmer and cook for 10-12 minutes, or until the noodles are tender.\n"
                       "Season the soup with salt and pepper to taste.\n"
                       "Remove the bay leaves and discard.\n"
                       "Serve the chicken noodle soup hot, garnished with fresh parsley.",

                       "Spaghetti Carbonara: \n"
                       ""
                       "Ingredients:\n"
                       "8 oz spaghetti\n"
                       "4 slices bacon, diced\n"
                       "2 cloves garlic, minced\n"
                       "2 large eggs\n"
                       "1/2 cup grated Parmesan cheese\n"
                       "Salt and pepper to taste\n"
                       "Fresh parsley for garnish\n"
                       ""
                       "Instructions:\n"
                       ""
                       "Cook the spaghetti according to package instructions until al dente. Drain and set aside,"
                       "reserve 1/2 cup of the pasta cooking water.\n"
                       "In a large skillet, cook the diced bacon over medium heat until crispy. \n"
                       "Remove the bacon from the skillet and set aside, leaving the bacon grease in the skillet.\n"
                       "Add the minced garlic to the skillet and cook for 1-2 minutes, or until fragrant.\n"
                       "In a small bowl, whisk together the eggs and grated Parmesan cheese.\n"
                       "Add the cooked spaghetti to the skillet with the garlic and toss to coat in the bacon grease.\n"
                       "Remove the skillet from the heat and quickly stir in the egg and cheese mixture, along with the cooked bacon.\n"
                       "If the sauce seems too thick, add some of the reserved pasta cooking water to thin it out.\n"
                       "Season the spaghetti carbonara with salt and pepper to taste.\n"
                       "Serve hot, garnished with fresh parsley.",

                       ]

        user_no = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        recipe = random.choice(recipe_list)
        user_choice = ""
        while user_choice not in user_no:
            user_choice = float(input("input your lucky number (1 - 10):"))
        print("the recipe for today is: \n", "\n", recipe)

    choice = input("input choice for programme: ")

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
    elif choice == "7":
        power_calculator()
    elif choice == "8":
        true_or_false()
    elif choice == "9":
        rock_paper_scissors()
    elif choice == "10":
        random_recipe_generator()
    else:
        print("please input the right choice.")
        main()


main()
# starts the whole programme since it cant be put inside the main function
# if put inside the main function the main function loops infinitely :]...
