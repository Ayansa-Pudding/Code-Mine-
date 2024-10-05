def power(set):
    elements=list(set)
    n= len(elements)
    
    size= 2 ** n
    power=[]
    for i in range (size):
        subset=[]
        
        for j in range(n):
            if i & (1<<j):
                subset.append(elements[j])
        power.append(subset)
    return power
set={99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,82}
result=power(set)
for subset in result:
    print(subset)