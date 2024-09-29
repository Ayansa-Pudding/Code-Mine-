# number=input("Enter your number: ")
# Original_number=number
# reversed_number=0
# while number>0:
#     digit= number % 10
#     reversed_number= reversed_number * 10 + digit
#     number //=10
# if Original_number== reversed_number:
#     print("This number is a palindrome")
# else:
#     print("This number is not a palindrome.")
largest=int(input("Enter your number(Larger): "))
smallest=int(input("Enter second number(Smallest): "))
while(smallest):
    GCD=smallest
    smallest=largest%smallest
    largest=GCD
print("Greatest Common Divisor: ", largest)