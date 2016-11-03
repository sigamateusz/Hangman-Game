import random
import os
os.system('clear') # clear screen

capitols = ["Berlin","Bratislava","Budapest","Dublin","London","Paris",
"Amsterdam","Oslo","Warsaw","Cracow"]
#random_capitol = 0


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
    count = random_capitol.count(n)
    if count == 0:
        print("You looseee..")
    else:
        for i in range(1,count+1):
            random_capitol_dashes[random_capitol.index(n)] = n
            random_capitol[random_capitol.index(n)] = 0


def user_input():
    '''get user input and convert to upper'''
    global user_letter
    global user_word
    get_user_input = input('Pick a letter or a word ')
    #if get_user_input.isdigit:
        #user_input()
    if len(get_user_input) >= 2:
        user_word = get_user_input
        user_word = user_word.upper()
        return user_word
    elif len(get_user_input) == 1:
        user_letter = get_user_input
        user_letter = user_letter.upper()
        return user_letter


def main():
    create_dashes_capitol()
    chech_user_input('A')
    print(random_capitol_dashes)
if __name__ == '__main__':
    main()
