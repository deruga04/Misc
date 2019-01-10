def memoized_cut_rod(p, n):
    r = []
    for i in range(n):
        r.append(0)

    for i in range(n):
        r[i] = int('-inf')

    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
    pass

def bottom_up_cut_rod(p, n):
    r = []
    cuts = [0] * (n + 1)
    
    r.append(0)

    for j in range(1, n + 1):
        local_max = 0
        local_index = 0
        for i in range(0, j):
            if (p[i] + p[j - i] > local_max):
                local_max = p[i] + p[j - i]
                cuts[j] = i
        r.append(local_max)

    return f'{r[n]} {cuts}'


print(bottom_up_cut_rod([1,2], 1))
print(bottom_up_cut_rod([0, 1, 2, 3, 2, 2, 6, 1, 2, 3, 10], 10))
print(bottom_up_cut_rod([0, 1, 2, 3, 2, 2, 6, 1, 2, 3, 10], 7))
print(bottom_up_cut_rod([0, 1, 2, 3, 2, 2, 6, 1, 2, 3, 10], 3))
print(bottom_up_cut_rod([0, 1, 2, 3, 2, 2, 6, 1, 2, 3, 10], 4))
