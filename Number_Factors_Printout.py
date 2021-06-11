###To get the factors of a number
##def factors(number):
##    ''''Prints the factors of a positive number in a list'''
##    f_list = []
##    for fact in range(1,number+1):
##        if number % fact == 0:
##            f_list.append(fact)
##    return f_list
##
##num = int(input ("Input\nPlease enter a positive number to get the factors\n"))
##answer = factors(num)
##print(f"Output\nThe factors are {answer}")


x = 0
y = 0
def f():
    x = 1
    y = 1
    class C:
        print(x, y)  # What does this print?
        x = 2
f()
