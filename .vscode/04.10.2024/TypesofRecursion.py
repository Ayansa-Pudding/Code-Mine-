
# #Head function: Call the function then do any operation
# def  head(n):
#     if n==0:
#         return
#     head (n-1)
#     print (n) 
# n=int(input("Enter your range: "))
# print(head(n))
# #Tail function: Opposite of Head
# def tail(n):
#     if n==0:
#         return
#     print (n)
#     tail (n-1)
# n=int(input("Enter your range: "))
# print(tail(n))
def incdec (n,num):
    if(n<1 or n>num):
        return
    print(n)
    incdec(n-1,num)
    print(n)
num=int(input("Enter your number: "))
incdec(num,num)