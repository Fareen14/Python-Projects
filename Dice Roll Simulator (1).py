import random
import time

roll_chances = 0
print("Type ROLL to roll the dice")
roll = input()

while roll_chances<5:
    print("Rolling dice....")
    time.sleep(1)
    roll_num = random.randint(1,6)
    print(str(roll_num))
    roll_chances += 1
    if roll_chances >= 5:
        print("Chances are over!")
        break
    print("Do you want to roll dice again?")
    roll_again = input()
    if not(roll_again == 'y' or roll_again == 'Y'):
        break

