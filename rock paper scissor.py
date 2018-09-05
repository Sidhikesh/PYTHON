import random


def rps():
    choice = random.randint(1, 3)
    if choice == 1:
        rock()
    elif choice == 2:
        paper()
    else:
        scissors()


# define funtion for rock
def rock():
    user_choice = input('1 for rock \n 2 for paper \n 3 for scissors')
    if user_choice == '1':
        print('YOU TIE. You chose Rock and the computer chose Rock')
        try_again()
    if user_choice == '2':
        print('YOU WON. You chose Paper and the computer chose Rock')
        try_again()
    if user_choice == '3':
        print('YOU LOSE. You chose Scissors and the computer chose Rock')
        try_again()
    else:
        print('Try Again')
        rock()


# define funtion for paper
def paper():
    user_choice = input('1 for rock \n 2 for paper \n 3 for scissors')
    if user_choice == '1':
        print('YOU LOSE. You chose Rock and the computer chose Paper')
        try_again()
    if user_choice == '2':
        print('YOU TIE. You chose Paper and the computer chose Paper')
        try_again()
    if user_choice == '3':
        print('YOU WIN. You chose Scissors and the computer chose Paper')
        try_again()
    else:
        print('Try Again')
        paper()


# define funtion for scissors
def scissors():
    user_choice = input('1 for rock \n 2 for paper \n 3 for scissors')
    if user_choice == '1':
        print('YOU WIN. You chose Rock and the computer chose scissors')
        try_again()
    if user_choice == '2':
        print('YOU LOSE. You chose Paper and the computer chose scissors')
        try_again()
    if user_choice == '3':
        print('YOU TIE. You chose Scissors and the computer chose scissors')
        try_again()
    else:
        print('Try Again')
        scissors()


# define funtion for try again
def try_again():
    choice = input('would you like to play? y/n')
    if choice == 'y' or choice == 'yes' or choice == 'Y':
        rps()
    elif choice == 'n':
        print('thanks for playing')
    else:
        print('Try Again')
        try_again()


rps()


