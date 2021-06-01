import random

turn=True

while turn:
    print(random.randint(1, 6))
    roll_again=input("Want to roll the dice again?(y/n):")
    if roll_again.lower() =="y":
        continue
    else:
        break
