def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    
    a1 = 1
    a2 = 2
    a3 = 3

    for i in range(n - 3):
        a = a2 + a3
        a3, a2 = a, a3

    return a

print(f(10))
