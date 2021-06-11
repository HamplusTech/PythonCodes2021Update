###Achermann Function
##m = int(input("Enter the value of m\n"))
##n = int(input("Enter the value of n\n"))
##if (nm == 0 ):
##    A = n +1
##elif (m > 0 and n == 0):
##    A = (m - 1, 1)
##elif (m > 0 and n > 0):
##    A = (m -1, (m,n - 1))

##for t in range(-27, 90, 3):
##    if (t >= 0):
##        y = - (3 * t * t ) + 5
##    elif (t < 0):
##        y = (3 * t *t) + 5
##    print(f"Y is = {y} when t is = {t}")

print("Plate number validator\n")
plateNumber = input("Please enter a plate number\n")
#consider validity of plate number
if (len(plateNumber) == 6 or len(plateNumber) == 7):
    #consider old plate number
    if plateNumber[0:3].isalpha():
        print("plate number is new")
    elif plateNumber[0:2].isalpha():
        print("plate number is old")
else:
    print ("plate number is not valid")
    
