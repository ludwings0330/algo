
def solution(board):
    row = len(board)
    col = len(board[0])
    answer = 0

    if row <= 1 or col <= 1:
        for r in range(row):
            for c in range(col):
                answer = max(answer, board[r][c])
        return answer

    for r in range(1, row):
        for c in range(1, col):
            if board[r][c] == 1:
                board[r][c] = 1 + min(board[r-1][c], board[r][c-1], board[r-1][c-1])
            answer = max(answer, board[r][c]**2)

    return answer


# 9, 4
board = [[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]], [[0,0,1,1],[1,1,1,1]]]

for b in board:
    print(solution(b))
