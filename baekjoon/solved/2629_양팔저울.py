import sys
sys.setrecursionlimit(10**9)
input = lambda: sys.stdin.readline().rstrip()

W = int(input())
weights = list(map(int, input().split()))
T = int(input())
beads = list(map(int, input().split()))
cache = [[-1]*(40001+500*W) for _ in range(W)]
MAX = (40001+500*W)

def solve(n, w):
    idx = (MAX + w) % MAX
    if w == 0:
        return 1
    if n == W:
        return 0

    if cache[n][idx] != -1:
        return cache[n][idx]

    cache[n][idx] = 0

    cache[n][idx] += solve(n+1, w + weights[n])
    cache[n][idx] += solve(n+1, w - weights[n])
    cache[n][idx] += solve(n+1, w)
    return cache[n][idx]

for target in beads:
    print('Y' if solve(0, target) else 'N', end = ' ')
