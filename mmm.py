arr=[2,4,6,8,10,12]
mean=sum(arr)/len(arr)

sorted_arr= sorted(arr)
n=len(sorted_arr)
median = (sorted_arr[n // 2] if n % 2 != 0

else (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2)

print ("Mean:", mean)

print ("Median:", median)
max_value=arr[0]
min_value=arr[0]
for num in arr:
    if num>max_value:
        max_value=num
    if num < min_value :
        min_value =  num
print("Maximum value:",max_value)
# print("Minimum value:", min_value)
if len(arr)<2:
    print("Array needs at leasttwo elements: ")
else:
    sorted_arr = sorted(arr, reverse=True)
    second_largest=sorted_arr[1]
    print("Second largest element: ", second_largest)