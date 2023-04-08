import random
import time


# Dots animation function
def animation_loading():
    for i in range(3):
        time.sleep(1)
        print("Loading" + "." * i)


# Get user's name and surname. Ensure that inputs are not empty strings.
while True:
    user_name = input("Provide your name: ")
    user_surname = input("Provide your surname: ")
    if user_name and user_surname:
        break
    else:
        print("Invalid input. Please enter a valid name and surname. ")

# Display game instructions
print(f"\nHello {user_name} {user_surname}!\n")
print("It is a Predictable Ball Game.")
print("Where you can provide any question and our ball will produce random answer.\n")

time.sleep(2)

# Get user's question. Ensure that input is not empty.
while True:
    your_question = input("Ask me anything: ")
    if your_question:
        break
    else:
        print("Invalid input. Please enter a valid question. ")

# Output processing message with loading dots animation.
print("\nYour question is being processed.")
animation_loading()

# Define the possible answers as a dictionary
answers = {
    1: "Yes, definetely.",
    2: "It is decidedly so.",
    3: "Without a doubt",
    4: "Wow, try jumping...",
    5: "Reply hazy, try again.",
    6: "Better not tell you now.",
    7: "My sources say no",
    8: "What a great turn.",
}


# Create random number from 1 to 8 and use it to to select an answer from a dictionary.
rnum = random.randint(1, 8)
answer = answers.get(rnum, "Ask again later...")

# Produce answer
print(f"\n{answer}\n")

# Add a clear separation between input and output sections
print("-" * 40)
