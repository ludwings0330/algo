'''
홍익 댄스 파티


'''

board = [list(input()) for _ in range(5)]

for c in range(len(board[0])):
    if board[2][c] == 'l':
        board[0][c] = '.'
        board[1][c] = 'o'
        board[2][c] = 'm'
        board[3][c] = 'l'
        board[4][c] = 'n'

    elif board[2][c] == 'm':
        board[0][c] = 'o'
        board[1][c] = 'w'
        board[2][c] = 'l'
        board[3][c] = 'n'
        board[4][c] = '.'


for r in range(5):
    print(''.join(board[r]))