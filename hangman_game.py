import random
import os
os.system('clear') # clear screen

capitols = ["Bratislava","Budapest","Dublin","London","Paris",
"Amsterdam","Oslo","Warsaw","Cracow"]
print(capitols)

random_capitol = capitols[random.randrange(0, len(capitols))]

random_capitol = random_capitol.upper()

print(random_capitol)

list(random_capitol)

print(list(random_capitol))

random_capitol_dashes = list(random_capitol)


def user_input():
    global user_letter
    global user_word
    get_user_input = input('Pick a letter or a word ')
    #if get_user_input.isdigit:
        #user_input()
    if len(get_user_input) >= 2:
        user_word = get_user_input
        return user_word
    elif len(get_user_input) == 1:
        user_letter = get_user_input
        return user_letter
