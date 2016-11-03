import random
import os
os.system('clear') # clear screen

capitols = ["Berlin","Bratislava","Budapest","Dublin","London","Paris",
"Amsterdam","Oslo","Warsaw","Cracow"]
random_capitol = 0


def create_dashes_capitol():
    global random_capitol
    random_capitol = capitols[random.randrange(0, len(capitols))]
    random_capitol = random_capitol.upper() # random capitol with uppercase
    random_capitol = list(random_capitol)
    random_capitol_dashes = random_capitol # split capitol
    print(random_capitol)
    for i in range(len(random_capitol_dashes)):
        random_capitol_dashes[i] = "_"
    print(random_capitol_dashes)


def chech_user_input(n):
    global random_capitol
    print()
    count = random_capitol.count(n)
    if count == 0:
        print("You looseee..")
    else:
        print("Excellent")


#def user_input():
#    get_user_input = input('Pick a letter or a word')
#    if float('')
#    if len(get_user_input) >= 2:
#        user_word = get_user_input




def main():
    create_dashes_capitol()
    chech_user_input('A')

if __name__ == '__main__':
    main()
