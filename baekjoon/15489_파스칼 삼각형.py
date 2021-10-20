import sys
input = lambda: sys.stdin.readline().rstrip()

R, C, W = map(int, input().split())

board = [[0]* (R + W) for _ in range(R + W)]
R -= 1
C -= 1

board[0][0] = 1

for r in range(len(board)-1):
    for c in range(len(board[r]) - 1):
        board[r][c] += board[r-1][c]
        board[r][c+1] += board[r-1][c]
answer = 0
for r in range(W):
    for c in range(r+1):
        answer += board[R+r][C+c]

print(answer)