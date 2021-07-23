import sys
sys.stdin.readline

N = int(input())
board = []
for i in range(N):
    line = list(map(int, input().rstrip().split()))
    board.append(line)

start = [0, 1]

dp = [[[0]*N for _ in range(N)] for __ in range(3)]

for c in range(1, N):
    if board[0][c] == 1:
        break
    dp[1][0][c] = 1

for r in range(1, N):
    for c in range(2, N):
        if board[r][c] == 0 and board[r-1][c] == 0 and board[r][c-1] == 0:
            dp[0][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]

        if board[r][c] == 0:
            dp[1][r][c] = dp[1][r][c-1] + dp[0][r][c-1]
            dp[2][r][c] = dp[2][r-1][c] + dp[0][r-1][c]


print(dp[0][-1][-1] + dp[1][-1][-1] + dp[2][-1][-1])
