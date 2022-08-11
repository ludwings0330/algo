import sys
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
names = [int(input()) for _ in range(N)]
cache = [[-1] * (M+2) for _ in range(N+2)]


# n번재 이름, r번째줄, c 위치일때
def solve(n, c):
    if n >= N:
        return 0
    if cache[n][c] != -1:
        return cache[n][c]

    # 다음줄에 이름쓰기
    cache[n][c] = solve(n+1, names[n]+1) + (M - c + 1)**2

    # 현재 위치에 이름을 넣고 같은 줄에서 시작
    if c + names[n] <= M:
        cache[n][c] = min(cache[n][c], solve(n + 1, c + 1 + names[n]))

    return cache[n][c]


print(solve(0, 0))
