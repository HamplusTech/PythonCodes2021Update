#A program to print the fibonacci sequence
print("The Input")
number = int(input("Please enter a number\n"))
print()


def fib(n):
    ''''Finds the fibonacci of a positive number'''
    f0, f1 = 0, 1

    if n == 0:
        return f0

    if n == 1:
        return f1

    return fib(n-1) + fib(n-2)

print("The Output")
for i in range(number):
    print(fib(i))


##number = int(input("Enter a positive integer\n"))
##print()
##print("The output")
##def fib(n):
##    '''Enter a positive integer to get the fibonacci sum'''
##    f0, f1 = 0,1
##    if n == 0:
##        return f0
##
##    if n == 1:
##        return f1
##    
##    a = (fib(n-1) + fib(n-2))
##    return a
##
##for i in range(number):
##    print(fib(i))
