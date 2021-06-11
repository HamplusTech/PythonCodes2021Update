def is_prime (n):
    '''Checks if n is a prime number. Returns True or False'''
    if n <= 1:
        return False

    for i in range(2,n):
        if n%i == 0:
            return False

    return True

def prime_print_out(n):
    '''Prints the prime numbers in the range of n'''
    primes = []
    for i in range(1,n):
        if is_prime(i):
            primes.append(i)
    yield primes
