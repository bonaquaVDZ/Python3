'''
Documentation and Explanation:
This script will generate password which will be based on your first date with your lovers.
This password will based on sum of fuctorialized date. 
'''

from math import factorial
from time import sleep

# Miscellaneous functions
def PrintFunction(Value):
    """ This function prints. """
    return print(Value)

def Factorialize(Numbers):
    """ Return factorials of a list of numbers. """
    return [factorial(num) for num in Numbers]

def SleepFunction(Time):
    """Suspend execution of a thread."""
    return sleep(Time)

# Miscellaneous variables for this script
Introduction = """ 
    Hello, my dear user!
    I am glad to see you here! I would propose you to introduce yourself.
    Please provide some infomation about yourself!
    I appreciate it very much! """

Awareness = """
    Please read carefully this passage.
    Be aware that you should use specified numbers from your first date with your girlfriend/boyfriend.
    
    Your instruction is following:
    *** Format of your first date has to be dd/mm/yyyy.
    *** First number of your date day has to be summed. (Ex: If your number is 23 (Answer: 5 (Sum of 2 and 3)))
    *** Second number of your manth date has to be summed. (Ex: See example above.)
    *** Third number of your year the same.
    
    In the end you should have three different numbers that you will put in my function.
    This function will create our date-specified password that we will be using in the future."""
    
Explanation = """
    Next step I am going to factorialize all of this numbers and give you a sum of all of them.
    This sum will be your new generated first-date password. """
    
Processing = "We are proccessing your information. Please be patient."


Appreciation = "I appreciate your efforts."


Separator = "-----------------------------------------------------------------------------------------------------------"

PrintFunction(Separator)
PrintFunction(Introduction)
PrintFunction(Separator)

SleepFunction(3)
name = str(input(">>> Please enter your name: "))
surname = str(input(">>> Please enter your surname: "))
PrintFunction(Separator)
PrintFunction(Processing)

SleepFunction(3)
PrintFunction("{} {}, thank you for beeing here!".format(name,surname))

SleepFunction(2.5)
PrintFunction(Separator)
print(Awareness)
PrintFunction(Separator)

SleepFunction(10)

# List of multiple integers  that separated by spaces
numbers = list(map(int,input(">>> Please enter three numbers separated by spaces: ").split()))


PrintFunction(f">>> Your list of numbers is: {numbers} ")
PrintFunction(Separator)

SleepFunction(3)
PrintFunction(Explanation)
PrintFunction(Separator)

SleepFunction(7)
PrintFunction("The factorial of {0} is {1}".format(numbers,Factorialize(numbers)))
PrintFunction(Separator)

SleepFunction(5)
password = sum(Factorialize(numbers))
PrintFunction("Sum of factorialized numbers is: {} ".format(password))
PrintFunction(Separator)

SleepFunction(5)
PrintFunction(f"{name} {surname} that was really a great job! Thank you for doing it together.")
PrintFunction("Lets use our new password in a future!")
Remembrance = """
Brief explanation what we have done before. 
Our password is {}.
This password made of your first-date that was factorialized and summed.""".format(password)
PrintFunction(Separator)

SleepFunction(5)
PrintFunction(f"{name} {surname}, see you in the next tutorials.")