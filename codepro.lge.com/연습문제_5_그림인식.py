import sys
input = sys.stdin.readline().rstrip()

N = int(input())
board = []

for _ in range(N):
    line = list(map(int, input().split()))
    board.append(line)

# 유일한 직사각형인지 확인
# 4 <= N <= 10
# 0 <= color <= 9

visit = [[False] * N for _ in range(N)]


def check(mr, mc):
    pass

for r in range(N):
    for c in range(N):
        if not visit[r][c]: # 아직 방문안함
            check(r, c, board[r][c])
            pass