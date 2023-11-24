import os
import random
from termcolor import colored
LINE = '-' * 70


def clear_screen():
    os.system('cls')


def welcome_message():
    print()
    print(colored(LINE , 'red') , end= ' ')
    print(colored("<<< WELCOME TO THE FLOWER OR ABSURD GAME >>>" , 'cyan' , attrs=['bold']) , end= ' ')
    print(colored(LINE , 'red'))
    print()


def chance_of_the_game():
    while True:
        user_chance = input('How meny times do you want to game? ')
        if not user_chance.isdigit() or int(user_chance) <= 0:
            print()
            print('The time of the game should be "positive number".')
            print('Please try again.')
            print(LINE)
        else:
            return int(user_chance)

      
def cups_of_the_game():
    while True:
        user_cups = input('How meny cups? ')
        if not user_cups.isdigit() or int(user_cups) <= 1:
            print()
            print('number of the cups shuold be postive number and more than 1 .')
            print('Please try again.')
            print(LINE)
        else:
            return int(user_cups)


def user_guess_of_game(cups):
    while True:
        user_guess = input(f'Guess of [1-{cups}]: ')
        if not user_guess.isdigit() or int(user_guess) <= 0 or int(user_guess) > cups:
            print()
            print(f'Your guess should be between 1 and {cups}')
            print(LINE)
        else:
            return int(user_guess)
            # agar user_guess (int) nabashad varede ife paein dar run_the_game nemishavad.


def do_you_want_game_again():
    while True:
        user_input = input('Do you want to game again?(y/n): ')
        if user_input.lower() in ['y' , 'n']:
            if user_input.lower() == 'y':
                run_the_game()
            else:
                print('\n')
                print(colored('<<< End of the game >>>' , 'green'))
                print(colored('<<< Thank you for choosing us >>>' , 'white'))
                print(colored('<<< Good luck >>>' , 'red')) 
                print('\n')
                return
        else:
            print()
            print('Invalid input. Please enter y = (yes) or n = (no)')
            print()


def run_the_game():
    clear_screen()
    welcome_message()
    cups = cups_of_the_game()
    print()
    chance = chance_of_the_game()
    ai_goal = random.randint(1,cups)
    word = 's'

    for i in range(chance):
        if chance - i == 1:
            word = ''
        print()    
        print(f'{chance - i} chance{word} left:')
        print()

        user_guess = user_guess_of_game(cups)
        # agar user_guess (int) nabashad varede ife paein nemishavad.
        if user_guess == ai_goal:
            print()
            print(colored('Your guess is right!' , 'green'))
            print() 
            print(colored('YOU WON!' , 'green'))
            print()
            return
        else:
            print()
            print(colored('Your guess is wrong.' , 'red'))
            print(LINE)

    print(colored('YOU LOST!' , 'red'))
    print()
    print(f'The correct answer is {ai_goal}')
    print(LINE)


run_the_game()
do_you_want_game_again()