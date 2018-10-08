

print('ROLLING A PAIR OF DICE')
def Dice():
    import random
    n=3 #no of chances
    input('Enter to roll die1 and die2')
    die1=random.randint(1,6)#rolling 1st die
    die2=random.randint(1,6)#rolling 2nd die
    total=die1+die2 
    for i in range(4):
        user_guess=int(input('Guess the sum '))
        if total== user_guess:
            print('YOU WON')
            print('You rolled a {} and a {}'.format(die1,die2))
            print('And the Total is {}'.format(total))
            try_again()
        else:
            print('YOU LOOSE \nYou have',n,'chances left')
            n=n-1
    try_again()
                                 

def try_again():
    choice = input('would you like to play? y/n')
    if choice == 'y' or choice == 'yes' or choice == 'Y':
        Dice()
    elif choice == 'n' or choice == 'no' or choice == 'N':
        print('Thanks for playing')
        
Dice()


