# def reverse_int(n):
#     if n > 0 :
#         return int (str(n)[::-1])
# number=int(input("Enter a number"))
# reversed_num = reverse_int(number)
# print("Reversed Integer:",reversed_num)       

# string= input("Enter a string")
# a= string[::-1]
# print(a)

n=int(input("Enter your Number: "))
def ciP(n):
    if(n<=0):
        return False
    if(n==1):
        return True
    if(n%4==0):
        return ciP(n/4)
if(ciP(n)):
    print("Power of 4")
else:
    print("Not Power of 4")
