"""PasswordGenerator."""
import secrets
from string import printable

# Removing whitespaces from printable
chars = printable
chars = chars.strip()

# Certain constraints for password generation
digits = int(input("Please enter the minimal amount of digits: "))
alphas = int(input("Please enter minimal amount of letters: "))
pwd_length = int(input("Preferred length of password: "))

# Creating of determined password based on constraints.
# Default: at least 1 lowercase letter
while True:
    pwd = str()
    for i in range(pwd_length + 1):
        pwd += "".join(secrets.choice(chars))
    if (
        any(c.islower() for c in pwd)
        and sum(c.isdigit() for c in pwd) >= digits
        and sum(c.isalpha() for c in pwd) >= alphas
    ):
        break

print("Length of your password is {}".format(pwd_length))
print("------------------------------------------------------")
print(
    ">>> Constraints:"
    "\n\t Default: at least 1 lowercase letter,"
    "\n\t User-determined: at least {} digits,"
    "\n\t User-determined: at least {} letters".format(digits, alphas)
)


print("\n>>> Your password: ", pwd)
