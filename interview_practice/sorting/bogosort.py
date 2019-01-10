import random

def bogosort(array):
    correct = array.sort()
    
    while not array == correct:
        random.shuffle(array)
        print(array)

    return array

print(bogosort([36, 99, 95, 70, 88, 16, 86, 5, 29, 55, 64, 9, 47, 44, 35, 97, 78, 58, 48, 26]))
