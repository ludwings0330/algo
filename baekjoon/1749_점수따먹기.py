import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

board = [[0] * (M+1) for _ in range(N+1)]
p_board = [[0] * (M+1) for _ in range(N+1)]

for r in range(1, N+1):
    s = list(map(int, input().split()))
    for c in range(1, M+1):
        p_board[r][c] = p_board[r][c-1] + s[c-1]
    for c in range(1, M+1):
        p_board[r][c] += p_board[r-1][c]

ans = 0
for r in range(1, N+1):
    for c in range(1, M+1):
        for rr in range(r, N+1):
            for cc in range(c, M+1):
                tmp = p_board[rr][cc] - p_board[r-1][cc] - p_board[rr][c-1] + p_board[r-1][c-1]
                ans = max(ans, tmp)

print(ans)
