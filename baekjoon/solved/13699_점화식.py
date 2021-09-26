import sys

cache = [-1] * (36)

n = int(input())
cache[0] = cache[1] = 1
cache[2] = 2
cache[3] = 5

def t(n):
    if cache[n] != -1:
        return cache[n]

    cache[n] = 0

    for k in range(n):
        cache[n] += t(k) * t(n-1-k)

    return cache[n]

print(t(n))
