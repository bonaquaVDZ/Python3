# Find all prime numbers in a specific range.
def prime_number(n):
    collector = []
    for num in range(2, n+1):
        for i in range(2, num):
            if num%i==0:
                break
        else:
            collector.append(num)
    return collector

print(prime_number(11))


