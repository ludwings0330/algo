'''
시작위치 대나무를 먹고 상하좌우, 현재위치보다 많은 대나무가 있는 지역으로 이동
최대한 많은 칸을 이동해야한다.
이동할 수 있는 칸의 수의 최대값을 출력

input :
4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8
예제 출력 1
4


ans:
4

'''

import sys
sys.setrecursionlimit(10**9)
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

cache = [[-1] * n for _ in range(n)]
visit = [[False]*n for _ in range(n)]
move = ((1, 0), (-1, 0), (0, 1), (0, -1))

def getPath(r, c):
    if 0 <= r < n and 0 <= c < n and not visit[r][c]:
        pass
    else:
        return 0


    if cache[r][c] != -1:
        return cache[r][c]

    visit[r][c] = True

    cache[r][c] = 1
    for i in range(len(move)):
        tr = r + move[i][0]
        tc = c + move[i][1]

        if 0 <= tr < n and 0 <= tc < n and board[tr][tc] > board[r][c]:
            cache[r][c] = max(cache[r][c], getPath(tr, tc) + 1)

    visit[r][c] = False
    return cache[r][c]

ans = 0
for r in range(n):
    for c in range(n):
        ans = max(ans, getPath(r, c))

print(ans)