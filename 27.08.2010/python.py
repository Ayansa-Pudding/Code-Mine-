# number=int(input("Input your number:"))
# digits=len(str(number))
# result_number=0
# temp=number
# while temp>0:
#     digit=temp %10
#     result_number +=digit **digits
#     temp //= 10
# if number == result_number: 
#     print("Your number is an armstrong number")
# else:
#     print("Your number is not an armstrong number")
# def print_factors(number):
#     print("The factors of", number,"are:")
#     for i in range(1, number+1):
#       if number % i==0:
#        print(i)
# number=int(input("Enter a number to see factors:"))
# print(print_factors(number))
def roman_to_int(a):
  roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
  int_form=0
  for i in range(len(a)):
    if i+1<len(a) and roman[a[i]]<roman[a[i+1]]:
      int_form-=roman[a[i]]
    else:
      int_form+=roman[a[i]]
  return int_form

a=input("enter a roman numeral")
print("interger form of",a,"is",roman_to_int(roman))