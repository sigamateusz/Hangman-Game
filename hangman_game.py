import sys
import random
import os
import time

os.system('clear') # clear screen


def load_list():
    global capitals
    global graphics
    f = open('capitals.txt', 'r')
    f_graphics = open('hangman_graphic.txt','r')
    capitals = f.read().splitlines()
    graphics = f_graphics.read()
    f.close()
    f_graphics.close()


def create_dashes_capital():
    """
    1. Picks a random capital from list
    2. Converts random capital to uppercase
    3. Saves string to list
    4. Copy to new id
    5. Converts to dash list
    """
    global CAPITOL_SAVE
    global random_capital
    global random_capital_dashes
    random_capital = capitals[random.randrange(0, len(capitals))] #1
    random_capital = random_capital.upper() #2
    random_capital = list(random_capital) #3
    CAPITOL_SAVE = random_capital[:] #4
    random_capital_dashes = random_capital[:]
    #print(random_capital)
    for i in range(len(random_capital_dashes)): #5
        if random_capital_dashes[i] == " ":
            continue
        else:
            random_capital_dashes[i] = "_"
    hangman_graphic()
    print("\n     {}\n".format(" ".join(random_capital_dashes)))


def check_user_input(n):
    """Check occurrence n in random_capital"""
    if len(n) == 1:
        count = random_capital.count(n)
        if count == 0:
            life()
            os.system('clear')
            hangman_graphic()
            print("\n     {}\n".format(" ".join(random_capital_dashes)))
        else:
            for i in range(1,count+1):
                # looking for index of n in random_capital
                random_capital_dashes[random_capital.index(n)] = n
                # set n in random_capital to 0
                random_capital[random_capital.index(n)] = 0
            os.system('clear')
            hangman_graphic()
            print("\n     {}\n".format(" ".join(random_capital_dashes)))
    else:
        n = list(n)
        if n == CAPITOL_SAVE:
            hangman_graphic()
            print("\n     {}\n".format(" ".join(CAPITOL_SAVE)))# random_capital_dashes = CAPITOL_SAVE[:]
            print("You win!!")
            play_again()
        else:
            life()


def user_input():
    '''get user input and convert to upper'''
    global health
    global n
    global user_letter
    global user_word
    global space_key
    count = 0
    print("Your life : {}".format(health))
    get_user_input = input('Pick a letter or a word :\t')
    count = get_user_input.count(" ")
    space_key = [0]*(count+1)
    if count > 0:
        for i in range(0,count):
            get_user_input = list(get_user_input)
            space_key[i] = get_user_input.index(" ")
            get_user_input.pop(space_key[i])
            get_user_input = "".join(get_user_input)
    if get_user_input.isdigit():
        user_input()
    elif get_user_input.isalnum() == False:
        user_input()
    elif len(get_user_input) < 1:
        user_input()
    elif len(get_user_input) >= 2:
        if count > 0:
            for i in range(0,count):
                get_user_input = list(get_user_input)
                get_user_input.insert(space_key[i]+i," ")
                get_user_input = "".join(get_user_input)
        user_word = get_user_input
        user_word = user_word.upper()
        n = user_word
    elif len(get_user_input) == 1:
        user_letter = get_user_input
        user_letter = user_letter.upper()
        n = user_letter


def life():
    global health
    health -= 1
    print("Sorry, you wrong.")
    time.sleep(1)
    os.system('clear') # clear screen
    hangman_graphic()
    print("\n     {}\n".format(" ".join(random_capital_dashes)))


def play_again():
    """Asks if user want to play again"""
    if health == 0:
        os.system('clear')
        print("\n     {}\n".format(" ".join(CAPITOL_SAVE)))
        print("\tYou looosee...")
    x = input("Do you want to play again? (y/n):\t")
    if x == 'y':
        os.system('clear')
        main()
    else:
        os.system('clear')
        sys.exit()


def hangman_graphic():
    global health
    if   health == 5:
        print(graphics[0:99])
    elif health == 4:
        print(graphics[100:199])
    elif health == 3:
        print(graphics[200:299])
    elif health == 2:
        print(graphics[300:399])
    elif health == 1:
        print(graphics[400:499])


def main():
    load_list()
    global health
    health = 5
    create_dashes_capital()
    while health > 0:
        user_input()
        check_user_input(n)
        if CAPITOL_SAVE == random_capital_dashes:
            break
    play_again()


if __name__ == '__main__':
    main()
