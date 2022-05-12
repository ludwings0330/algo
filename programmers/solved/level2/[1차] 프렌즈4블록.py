move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def solution(row, col, board):
    answer = 0
    board = [list(s) for s in board]
    has_square = True

    # repeat while there are removed blocks
    while has_square:
        has_square = False
        remove_pos = []

        for r in range(row - 1):
            for c in range(col - 1):
                if board[r][c] != '@' and board[r][c] == board[r][c+1] == board[r+1][c] == board[r+1][c+1]:
                    has_square = True
                    remove_pos.append([r, c])
                    remove_pos.append([r, c+1])
                    remove_pos.append([r+1, c])
                    remove_pos.append([r+1, c+1])

        for r, c in remove_pos:
            board[r][c] = '@'

        for r in range(row-1, 0, -1):
            for c in range(col):
                if board[r][c] == '@':
                    change_r = r - 1
                    while change_r > 0 and board[change_r][c] == '@':
                        change_r -= 1
                    board[r][c], board[change_r][c] = board[change_r][c], board[r][c]

    # count number of removed blocks
    for r in range(row):
        for c in range(col):
            if board[r][c] == '@':
                answer += 1

    return answer


m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

print(solution(m, n, board))