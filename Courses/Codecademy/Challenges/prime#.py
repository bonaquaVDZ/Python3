"""Check up whether it is prime number or not"""

def prime_checker(n):
    if n%n==0 and n//1 == n:
        return f'it is a prime number {n}'
    else:
        return f'it is not a prime number {n}'

print(prime_checker(3)) # Prime
print(prime_checker(10)) # Not Prime


def prime_checker(n):
    """
    Checks if the given number is prime.

    Args:
        n (int): The input number.

    Returns:
        str: A string indicating whether the number is prime or not.
    """
    if n < 2:
        return f'{n} is not a prime number'
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return f'{n} is not a prime number'
    return f'{n} is a prime number'

# In this optimized version of the function, we first check if the input number is less than 2, 
# which is not a prime number. Then, we iterate over all the numbers from 2 to the square root of the input number 
# (inclusive) and check whether the input number is divisible by any of them. If it is, 
# then the input number is not a prime number and we return a string indicating that. 
# If none of the numbers divide the input number, then the input number is a prime number and 
# we return a string indicating that
