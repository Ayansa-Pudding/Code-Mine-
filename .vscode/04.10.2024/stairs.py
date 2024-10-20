# def ways(stairs):
#     if stairs<0:
#         return 0
#     if stairs==0:
#         return 1
#     twosteps=0
#     onestep=0
#     if (stairs>=2):
#         twosteps=ways(stairs-2)
#     onestep= ways(stairs-1)
#     return twosteps+onestep
# stairs= int(input("Enter Your Number: "))
# print("Number of ways to climb stairs: ", ways(stairs))