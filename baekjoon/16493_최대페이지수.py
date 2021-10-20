import sys
sys.setrecursionlimit(10**9)

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
# N : 남은기건
# M : 챕터수

chapters = []
for _ in range(M):
    n, page = map(int, input().split())
    chapters.append([n, page])

cache = [[-1] * M for _ in range(N+1)]
'''
남은 기간동안 읽을 수 있는 최대 페이지
N : 남은 기간
M : 챕터수
[n, page]
[읽는데 걸리는 시간, 페이지 수]

현재 챕터를 읽거나 읽지않거나 두가지 선택이 가능하다.

solve(n, i) -> 남은 기간이 n일 이고 현재 챕터가 i일 때 읽을 수 있는 최대 페이지를 반환한다.

1. 현재 챕터를 읽는다.
    현재 챕터를 읽으면 -> solve(n - 읽는데 걸리는 시간, i+1) + 페이지수
2. 현재 챕터를 읽지 않는다.
    현재 챕터를 읽지않으면 -> solve(n, i+1)

'''

def solve(n, i):
    if i == M:
        return 0

    if cache[n][i] != -1:
        return cache[n][i]

    cache[n][i] = 0
    if n - chapters[i][0] >= 0:
        cache[n][i] = max(cache[n][i], solve(n - chapters[i][0], i+1) + chapters[i][1])
    cache[n][i] = max(cache[n][i], solve(n, i+1))

    return cache[n][i]

print(solve(N, 0))