import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 5)
N, M = map(int, input().split())
cache = [-1] * (N+1)
MOD = 10 ** 9 + 7


def solve(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    if cache[n] != -1:
        return cache[n]

    cache[n] = 0
    cache[n] = (solve(n-1) + solve(n-M)) % MOD

    return cache[n]


print(solve(N))
