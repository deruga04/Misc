def quicksort(a):
    if len(a) <= 1:
        return a

    left = []
    right = []
    equal = []
    
    pivot = a[-1]
    for num in a:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)

    return quicksort(left) + equal + quicksort(right)

array = [5, 10, 3, 12, 5, 5, 6]
print(quicksort(array))
