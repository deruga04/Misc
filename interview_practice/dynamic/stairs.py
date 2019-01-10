# You can climb 1, 2, 3, or 4 stairs at a time. How many ways can you climb exactly 20 stairs.

def f(N):
    r = 0
    if N == 0:
        return 1
    if N < 0:
        return 0

    r += f(N - 1) + f(N - 2) + f(N - 3) + f(N - 4)
    return r
   
s = [1, 2, 3, 4]
print(f(20)) # 283953 yes that is the answer, I couldn't believe it either
