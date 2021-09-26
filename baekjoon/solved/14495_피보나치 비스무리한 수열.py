cache = [-1] * (117)
cache[1] = cache[2] = cache[3] = 1

# f(n) = f(n-1) + f(n-3)

n = int(input())

def fibo(n):
    if cache[n] != -1:
        return cache[n]

    cache[n] = 0
    cache[n] = fibo(n-1) + fibo(n-3)

    return cache[n]

print(fibo(n))

