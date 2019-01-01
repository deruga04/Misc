# Suppose we had a list S and a number N. How can we find out whether there is a subset in S that
# adds up to N?

def f(N, S):
    r = 0
    if N == 0:
        return 1
    if not S:
        return 0

    for num in S:
        print(f'{N} {S}')
        r += f(N - num, remove(S, num))
    return r

# Removes an element a from list s. I need to write this because python's built-in remove is a
# morceau de merde
# Warning: may cause 1-off error because this isn't tested.
# @param s - list
# @param a - element to be removed
# @return s - list without the element a
def remove(s, a):
    index = 0
    for i in range(len(s)):
        if s[i] == a:
            index = i
    return s[0:i] + s[i + 1:len(s) + 1]
    
s = [4, 7, 11, 9, 45]
print(f(76, s))
