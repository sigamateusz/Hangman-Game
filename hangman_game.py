import random
import os
os.system('clear') # clear screen

capitols = ["Berlin","Bratislava","Budapest","Dublin","London","Paris",
"Amsterdam","Oslo","Warsaw","Cracow"]
n = 0
life = 5

def create_dashes_capitol():
    global random_capitol
    global random_capitol_dashes
    random_capitol = capitols[random.randrange(0, len(capitols))]
    random_capitol = random_capitol.upper() # random capitol with uppercase
    random_capitol = list(random_capitol)
    random_capitol_dashes = random_capitol[:]# copy to new id
    print(random_capitol)
    for i in range(len(random_capitol_dashes)):
        random_capitol_dashes[i] = "_"
    print(random_capitol_dashes)


def chech_user_input(n):
    """Check occurrence n in random_capitol"""
    count = random_capitol.count(n)
    if count == 0:
        print("You looseee..")
    else:
        for i in range(1,count+1):
            # looking for index of n in random_capitol
            random_capitol_dashes[random_capitol.index(n)] = n
            # set n in random_capitol to 0
            random_capitol[random_capitol.index(n)] = 0


def user_input():
    '''get user input and convert to upper'''
    global n
    global user_letter
    global user_word
    get_user_input = input('Pick a letter or a word ')
    if get_user_input.isdigit():
        user_input()
    elif get_user_input.isalnum() == False:
        user_input()
    elif len(get_user_input) < 1:
        user_input()
    elif len(get_user_input) >= 2:
        user_word = get_user_input
        user_word = user_word.upper()
        n = user_word
        return #user_word
    elif len(get_user_input) == 1:
        user_letter = get_user_input
        user_letter = user_letter.upper()
        n = user_letter
        return #user_letter

def life(arg):
    arg -= 1
    life = arg

def main():
    create_dashes_capitol()
    user_input()
    chech_user_input(n)
    print(random_capitol_dashes)
if __name__ == '__main__':
    main()
