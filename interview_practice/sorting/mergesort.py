def merge(list1, list2):
    r = []

    while list1 and list2:
        r.append(list1.pop(0)) if list1[0] < list2[0] else r.append(list2.pop(0))

    return r + list1 + list2

def mergesort(array):
    if len(array) == 1:
        return array

    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


a = [3, 6, 8]
b = [1, 4, 8]

print(merge(a,b))

print(mergesort([17, 19, 11, 5, 9, 20, 12, 1, 14, 10, 6, 4, 15, 18, 16]))
