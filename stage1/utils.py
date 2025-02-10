### NUMBER CLASSIFIER ###

def is_prime(n):
    #Checks if number is prime.
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    #Checks if number is a perfect number.
    return n > 0 and sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    #Checks if number is an Armstrong number.

    numStr = str(abs(n)) 
    power = len(numStr)
    return sum(int(digit) ** power for digit in numStr) == abs(n)


def is_even(n):
    #Checks if a number is even.
    return n % 2 == 0


