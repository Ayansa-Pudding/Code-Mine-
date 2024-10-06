# def fac(n):
#     if (n==1 or n==-1):
#         return 1
#     return n*fac(n-1)
# n=int(input("Enter your number:"))
# print(fac(n))

def Queu(n):
    if n>10:
        return
    print(n)
    Queu(n+1)
Queu(2)