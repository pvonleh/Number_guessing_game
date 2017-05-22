# Prince D. Vonleh
# pvonleh@gmail.com

import random


def play_again():
    play_again = input("Do you want to paly again? Y/n: ")
    if play_again != 'n':
        game()
    else:
        print("Bye!")
def easy_mode():
    # generate a random number between 1 and 10
    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 5:
        try:
            # get a number guess from the player
            guess = int(input("Guess a number between 1 and 10: "))
        # compare guess to secret number
        except ValueError:
            print("{} isn't a number".format(guess))
        else:
            if guess == secret_num:
                print("You got it! My number was {}".format(secret_num))
                play_again()
            elif guess < secret_num:
                print("The number is less than {}".format(guess))
            elif guess > secret_num:
                print("The number is greater than {}".format(guess))
            elif guess < 1 and guess > 10:
                print("Remember the number you guess have to be between 1 and 10!")
                break
            else:
                print("That's not it!")
            guesses.append(guess)
            play_again()

def  med_mode():
    # generate a random number between 1 and 10
    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 3 :
        try:
            # get a number guess from the player
            guess = int(input("Guess a number between 1 and 10: "))
        # compare guess to secret number
        except ValueError:
            print("{} isn't a number".format(guess))
        else:
            if guess == secret_num:
                print("You got it! My number was {}".format(secret_num))
                play_again()
            elif guess < secret_num:
                print("The number is less than {}".format(guess))
            elif guess > secret_num:
                print("The number is greater than {}".format(guess))
            elif guess < 1 and guess > 10:
                print("Remember the number you guess have to be between 1 and 10!")
                break
            else:
                print("That's not it!")
            guesses.append(guess)
            play_again()
def exp_mode():
    # generate a random number between 1 and 10
    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 1:
        try:
            # get a number guess from the player
            guess = int(input("Guess a number between 1 and 10: "))
        # compare guess to secret number
        except ValueError:
            print("{} isn't a number".format(guess))
        else:
            if guess == secret_num:
                print("You got it! My number was {}".format(secret_num))
                play_again()
            elif guess < secret_num:
                print("The number is less than {}".format(guess))
            elif guess > secret_num:
                print("The number is greater than {}".format(guess))
            elif guess < 1 and guess > 10:
                print("Remember the number you guess have to be between 1 and 10!")
                break
            else:
                print("That's not it!")
            guesses.append(guess)
            play_again()
def game():
    mode = int(input(""" 
          DIFFICULTY:
          Select 1 for easy.
          Select 2 for medium.
          Select 3 for expert.
          >>"""))
    if mode == 1:
        easy_mode()
    elif mode == 2:
        med_mode()
    elif mode == 3:
        exp_mode()
    elif mode > 3 or mode < 1:
        print("The mode has to be between 1 & 3.")
        play_again()
    else:
        print("Bye!")
game()