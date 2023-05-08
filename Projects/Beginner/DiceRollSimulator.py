from random import randint
from time import sleep

print("")
print(
    "Hello dear user, this is the easiest game where you have the chance "
    "to roll the die or exit the game. "
    "Keep in mind that you must choose 'yes' or 'no'."
)
sleep(2)
print("")

nums_collector = []

while True:
    reply = str(input("Would you roll a dice? \nYour answer: "))
    if reply == "yes" or reply == "Yes":
        print("Dice rolling...")
        sleep(1.0)
        print("Dice rolling...")
        sleep(1.3)
        print("Dice rolling...")
        sleep(1.5)
        random_roll = randint(1, 6)
        print("Your number: ", random_roll)
        nums_collector.append(random_roll)
        reply = str(input("Would you play again? \nYour answer: "))
        if reply == "yes" or reply == "Yes":
            print("Dice rolling...")
            sleep(1.0)
            print("Dice rolling...")
            sleep(1.3)
            print("Dice rolling...")
            sleep(1.5)
            random_roll = randint(1, 6)
            print("Your number: ", random_roll)
            nums_collector.append(random_roll)
        elif reply == "no" or reply == "No":
            sleep(1.0)
            print("")
            print("You chose to exit the game!")
            print("Goodbye!")
            break
        else:
            sleep(1.0)
            print("")
            print("You chose neither yes nor no.")
            print("Answer could be 'Yes/yes' or 'No/no'.")
    elif reply == "no" or reply == "No":
        sleep(1.0)
        print("")
        print("You chose to exit the game!")
        print("Goodbye!")
        break
    else:
        sleep(1.0)
        print("")
        print("You chose neither yes nor no.")
        print("Answer could be 'Yes/yes' or 'No/no'")

sleep(1.0)
print("")
print(
    "These are all your random numbers after rolling the dice: ",
    nums_collector,
)
