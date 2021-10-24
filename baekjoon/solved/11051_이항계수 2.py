import sys
sys.setrecursionlimit(10**9)

N, K = map(int, input().split())
DIV = 10**4 + 7
cache = [[-1] * (K+1) for _ in range(N+1)]

'''
(n k) = (n, n-k)
'''
def bino(n, k):
    if n < k: n, k = k, n
    if k == 0 or n == k:
        return 1

    if cache[n][k] != -1:
        return cache[n][k]

    cache[n][k] = bino(n-1, k) + bino(n-1, k-1)
    cache[n][k] %= DIV

    return cache[n][k]

print(bino(N, K))

