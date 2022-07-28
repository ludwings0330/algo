board = [['_'] * 4 for _ in range(4)]

move = ((1, 0), (-1, 0), (0, 1), (0, -1),(1, 1), (-1, 1), (1, -1), (-1, -1))

for _ in range(3):
    r, c = map(int, input().split())
    board[r][c] = '#'
    for dr, dc in move:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < 4 and 0 <= nc < 4 and board[nr][nc] != '#':
            board[nr][nc] = '@'

for r in range(4):
    for c in range(4):
        print(board[r][c],end='')
    print()
