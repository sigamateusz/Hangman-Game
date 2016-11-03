import random
import os
os.system('clear') # clear screen

capitols = ["Berlin","Bratislava","Budapest","Dublin","London","Paris",
"Amsterdam","Oslo","Warsaw","Cracow"]
print(capitols)

random_capitol = capitols[random.randrange(0, len(capitols))]

print(random_capitol)

list(random_capitol)

print(list(random_capitol))

random_capitol_dashes = list(random_capitol)
