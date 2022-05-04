def rotate(board, pos):
    min_value = float('inf')

    y1, x1 = pos[0]
    x1 -= 1
    y1 -= 1
    y2, x2 = pos[1]
    x2 -= 1
    y2 -= 1

    move = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    current = board[y1][x1]
    next_val = 0
    for col in range(x1 + 1, x2):
        next_val = board[y1][col]
        min_value = min(min_value, current)
        board[y1][col] = current
        current = next_val
    for row in range(y1, y2):
        next_val = board[row][x2]
        min_value = min(min_value, current)
        board[row][x2] = current
        current = next_val
    for col in range(x2, x1, -1):
        next_val = board[y2][col]
        min_value = min(min_value, current)
        board[y2][col] = current
        current = next_val
    for row in range(y2 , y1-1, -1):
        next_val = board[row][x1]
        min_value = min(min_value, current)
        board[row][x1] = current
        current = next_val

    return min_value


def solution(rows, columns, queries):
    answer = []
    board = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]

    for x1, y1, x2, y2 in queries:
        min_value = rotate(board, [[x1, y1], [x2, y2]])
        answer.append(min_value)

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
