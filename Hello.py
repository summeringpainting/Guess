import random
import time

print("hi")
loto = input("Pick a number from 1 to 3: ")
print("You picked " + loto + " Good For You!")
time.sleep(1)
loto_num = int(loto)
luck = random.randint(0, 3)
def loto_calc(loto_num, luck):
    while(loto_num != luck):
        while loto_num > 0 and loto_num < 3:
            print("close")
            loto = input("Pick a number from 1 to 3: ")
        else:
            print("Not Close")
            loto = input("Pick a number closer from 1 to 3: ")
    else:
        print("win")
print(loto_calc(loto_num, luck))
