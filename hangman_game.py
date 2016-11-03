import sys
import random
import os
os.system('clear') # clear screen

capitols = ["Be rlin","Brati slava","Buda pest","Dub lin","Lond on","P aris",
"Amste rdam","Os lo","Wa rsaw","Cra cow"]
n = 0
health = 0

def create_dashes_capitol():
    """
    1. Picks a random capitol from list
    2. Converts random capitol to uppercase
    3. Saves string to list
    4. Copy to new id
    5. Converts to dash list
    """
    global CAPITOL_SAVE
    global random_capitol
    global random_capitol_dashes
    random_capitol = capitols[random.randrange(0, len(capitols))] #1
    random_capitol = random_capitol.upper() #2
    random_capitol = list(random_capitol) #3
    CAPITOL_SAVE = random_capitol[:] #4
    random_capitol_dashes = random_capitol[:]
    print(random_capitol)
    for i in range(len(random_capitol_dashes)): #5
        if random_capitol_dashes[i] == " ":
            continue
        else:
            random_capitol_dashes[i] = "_"
    print("     {}".format(" ".join(random_capitol_dashes)))


def check_user_input(n):
    """Check occurrence n in random_capitol"""
    if len(n) == 1:
        count = random_capitol.count(n)
        if count == 0:
            life()
            os.system('clear')
            print("     {}".format(" ".join(random_capitol_dashes)))
        else:
            for i in range(1,count+1):
                # looking for index of n in random_capitol
                random_capitol_dashes[random_capitol.index(n)] = n
                # set n in random_capitol to 0
                random_capitol[random_capitol.index(n)] = 0
            os.system('clear')
            print("     {}".format(" ".join(random_capitol_dashes)))
    else:
        n = list(n)
        if n == CAPITOL_SAVE:
            print("     {}".format(" ".join(CAPITOL_SAVE)))# random_capitol_dashes = CAPITOL_SAVE[:]
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
    count = 0
    global space_key
    print("Your life : {}".format(health))
    get_user_input = input('Pick a letter or a word ')
    count = get_user_input.count(" ")
    if count > 0:
        get_user_input = list(get_user_input)
        space_key = get_user_input.index(" ")
        get_user_input.pop(space_key)
        get_user_input = "".join(get_user_input)
    if get_user_input.isdigit():
        user_input()
    elif get_user_input.isalnum() == False:
        user_input()
    elif len(get_user_input) < 1:
        user_input()
    elif len(get_user_input) >= 2:
        if count > 0:
            get_user_input = list(get_user_input)
            get_user_input.insert(space_key," ")
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


def play_again():
    """Asks if user want to play again"""
#    os.system('clear')
    if health == 0:
        print("You looosee...")
    x = input("Do you want to play again? (y/n)")
    if x == 'y':
        os.system('clear')
        main()
    else:
        os.system('clear')
        sys.exit()

def main():
    global health
    health = 5
    create_dashes_capitol()
    while health > 0:
        user_input()
        check_user_input(n)
        if CAPITOL_SAVE == random_capitol_dashes:
        #    print("     {}".format(" ".join(CAPITOL_SAVE)))
            break
    play_again()

if __name__ == '__main__':
    main()
