"""Topics:math.log,secrets.randbelow,time.sleep,input,for,if."""
import math
from secrets import randbelow
from time import sleep

print("")
print("Game: Guess the number")
print(
    "The main goal of the project is to create a program that randomly select a number "
    "in a range then the user has to provide as input."
)
print("")
# Taking inputs
upper_value = int(input("Please provide an upper bound for the random number: "))
sleep(1)
print(f"Random number will be between 0 and {upper_value}")

# Evaluate how many chances you will have
chances = round(math.log(upper_value - 0, 2))
print(f"You've only {chances} chances to guess the number.")


# while True:
for i in range(0, chances):
    # Taking inputs
    our_num = int(input("\nPlease enter your number: "))
    rand_num = randbelow(upper_value + 1)

    sleep(1)
    if our_num == rand_num:
        print("")
        print("Processing ...")
        sleep(1)
        print("Processing ...")
        sleep(1)
        print("Processing ...")
        sleep(1)
        print(f"\n\tMy Congratulations you did it in {i+1} try.")
        print("--------------------------------")
        print("\tYour number is ", our_num)
        print("\tConceived number is ", rand_num)
        print("--------------------------------")
        sleep(1)
        print("\n\tGame is over.")
        break
    else:
        print("")
        print("Processing ...")
        sleep(1)
        print("Processing ...")
        sleep(1)
        print("Processing ...")
        sleep(1)
        print("\n\tSorry, but you didn't guess the number.")
        print(f"\tConceived number was ", rand_num)

if our_num != rand_num:
    print("\nProgram terminates.")
