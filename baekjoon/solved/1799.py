import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

move = ((1, 1), (-1, -1), (1, -1), (-1, 1))
def putBS(r, c, type): # -1 놓기 1 빼기
    board[r][c] += type
    for i in range(4):
        dr = move[i][0]
        dc = move[i][1]

        for k in range(1, N):
            tr = r + dr*k
            tc = c + dc*k
            if 0 <= tr < N and 0 <= tc < N:
                board[tr][tc] += type
def solve(pick, n):
    global ret
    ret = max(ret, pick)
    for index in range(n, N*N):
        r = index // N
        c = index % N
        if board[r][c] > 0:
            putBS(r, c, -1)
            solve(pick+1, index+1)
            putBS(r, c, 1)
ret = 0
solve(0, 0)
print(ret)