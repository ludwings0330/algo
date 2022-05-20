import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    row, col = map(int, input().split())
    board = [list(input()) for _ in range(row)]

    for r in range(row-1, 0, -1):
        for c in range(col):
            if board[r][c] == '.':
                # pull stone if cell is empty
                for rr in range(r, -1, -1):
                    if board[rr][c] == 'o':
                        break
                    if board[rr][c] == '*':
                        board[r][c], board[rr][c] = board[rr][c], board[r][c]
                        break

    for line in board:
        print(''.join(line))
    print()
