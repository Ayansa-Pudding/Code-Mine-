
# arr.reverse()
# print(arr)
def left_rotate(arr, d):
    n = len(arr)
    d = d % n 
    return arr[d:] + arr[:d]
arr = [1, 2, 3, 4, 5]
rotated_array = left_rotate(arr, 2)
print(rotated_array) 

def right_rotate(arr, d):
    n = len(arr)
    d = d % n 
    return arr[-d:] + arr[:-d]
arr = [1, 2, 3, 4, 5]
rotated_array = right_rotate(arr, 2)
print(rotated_array) 