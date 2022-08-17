import sys
input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(R)]

for r in range(1, R):
    board[r][0] += board[r-1][0]
for c in range(1, C):
    board[0][c] += board[0][c-1]

for r in range(1, R):
    for c in range(1, C):
        board[r][c] += max(board[r-1][c], board[r][c-1])

print(board[-1][-1])
