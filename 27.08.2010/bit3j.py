def power2(number):
    if (number ==0):
        return 0
    if ((number &(~(number-1)))==number):
        return 1
    return 0
number = int(input("enter the number:"))

if (power2((number))):
    print("\n The number is power 2")
else:
    print("\n The number is not power 2")