##def print_decor(func):
##    print ("------------")
##    func()
##    print ("------------")
##
##def print_hello():
##    print ("Hello World ")
##


def func(f):
    def wrapper():
        print ("Started")
        f()
        print("Ended")

    return wrapper

@func
def func2():
    print("I am func2")


def func3():
    print ("I am func3")

func2()

func3 = func(func3)
func3()
