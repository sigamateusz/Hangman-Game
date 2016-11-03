import random
import os
os.system('clear') # clear screen

capitols = ["Berlin","Bratislava","Budapest","Dublin","London","Paris",
"Amsterdam","Oslo","Warsaw","Cracow"]

def create_dashes_capitol():
    random_capitol = capitols[random.randrange(0, len(capitols))]
    random_capitol = random_capitol.upper() # random capitol with uppercase
    random_capitol = list(random_capitol)
    random_capitol_dashes = random_capitol # split capitol
    for i in range(len(random_capitol_dashes)):
        random_capitol_dashes[i] = "_"
    print(random_capitol_dashes)

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


if __name__ == '__main__':
    main()
