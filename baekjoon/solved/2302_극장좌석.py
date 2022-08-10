import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())

seat = [0] * (N+1)
cache = [-1] * N

for _ in range(M):
    seat[int(input()) - 1] = 1


def solve(n):
    if n == N:
        return 1
    elif n == N+1:
        return 0

    if cache[n] != -1:
        return cache[n]

    # 고정석이라면 옆자리와 자리를 바꿀 수 없음
    if seat[n] == 1:
        return solve(n+1)

    cache[n] = 0
    # 옆자리와 자리를 바꾸지 않음
    cache[n] += solve(n+1)
    # 옆자리와 자리를 바꿈 (VIP 면 불가)
    if seat[n+1] == 0:
        cache[n] += solve(n+2)

    return cache[n]


print(solve(0))
