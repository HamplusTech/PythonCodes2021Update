#A program to check if a number is a prime
number = int(input("Please enter a positive number\n"))

def is_prime(num):
    '''Checks if a positive number is a prime number'''
    if num == 0:
        return False

    if num == 1:
        return False

    for fact in range(2,num):
        if num % fact == 0:
            return False

    return True

answer = is_prime(number)
if answer:
    print (f"The number, {number} is a prime number")
else:
    print (f"The number, {number} is not a prime number")
