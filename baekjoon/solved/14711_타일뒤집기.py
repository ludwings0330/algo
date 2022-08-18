import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())

tile = ['.', '#']
board = [['.'] * N for _ in range(N)]
ans_board = [['.'] * N for _ in range(N)]
ans_board[0] = list(input())
board[0] = ans_board[0][:]
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def turn(r, c):
    for dr, dc in move:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < N:
            board[nr][nc] = '.' if board[nr][nc] == '#' else '#'


for c in range(N):
    if ans_board[0][c] == '#':
        board[0][c] = '.' if board[0][c] == '#' else '#'
        turn(0, c)

for r in range(1, N):
    for c in range(N):
        # 위가 black 이라면 해당 칸을 반드시 눌러야한다.
        if board[r-1][c] == '#':
            turn(r, c)
            ans_board[r][c] = '#'

for r in range(N):
    print(''.join(ans_board[r]))
