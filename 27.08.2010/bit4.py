# def swap(a,b):
#   a=a^b
#   b=a^b
#   a=a^b
#   print("After swapping; a=",a,"and b=", b)
# swap(24,17)
def power(set):
    elements=list(set)
    n= len(elements)
    
    size= 2 ** n
    power=[]
    for i in range (size):
        subset=[]
        
        for j in range(n):
            if i and (1<<j):
                subset.append(elements[j])
        power.append(subset)
    return power

set={1 ,2 ,3}
result=power(set)
for subset in result:
    print(subset)