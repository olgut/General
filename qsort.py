def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(left)
    print(middle)
    print(right)
    print("loop number = X")
    return quicksort(left) + middle + quicksort(right)

print('\r\nResult = ', quicksort([3,6,8,10,11,1,2,1]))
