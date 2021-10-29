'''
4 4
0100
0111
1110
0010

4
'''

import sys
input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(R)]

for r in range(1, R):
    for c in range(1, C):
        if board[r][c] != 0:
            board[r][c] += min(board[r-1][c], board[r][c-1], board[r-1][c-1])

ans = 0
for r in range(R):
    for c in range(C):
        ans = max(ans, board[r][c])

print(ans**2)