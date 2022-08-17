import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
blocked = set()

cache = [[-1] * (N+1) for _ in range(N+1)]


for _ in range(M):
    set.add(int(input()))


def solve(n, x):
    if n == N:
        return 0
    if x < 0 or n > N:
        return float('inf')

    if cache[n][x] != -1:
        return cache[n][x]

    cache[n][x] = float('inf')

    if 0 <= n + x - 1 <= N and n+x-1 not in blocked:
        cache[n][x] = min(cache[n][x], solve(n+x-1, x-1) + 1)
    if 0 <= n + x <= N and n+x not in blocked:
        cache[n][x] = min(cache[n][x], solve(n+x, x) + 1)
    if 0 <= n + x + 1 <= N and n+x+1 not in blocked:
        cache[n][x] = min(cache[n][x], solve(n+x+1, x+1) + 1)

    return cache[n][x]


print(solve(2, 1)+1)