def solution(line):
    answer = []
    pos = []
    min_x, min_y, max_x, max_y = [float('inf'), float('inf'), float('-inf'), float('-inf')]
    for i in range(len(line) - 1):
        for j in range(i+1, len(line)):
            A, B, E = line[i]
            C, D, F = line[j]
            if A*D - B*C == 0:
                continue

            x = (B*F - E*D)/(A*D - B*C)
            y = (E*C - A*F)/(A*D - B*C)
            if x == int(x) and y == int(y):
                x, y = int(x), int(y)
                pos.append([x, y])
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)

    board = [['.'] * (max_x - min_x + 1) for _ in range(min_y, max_y + 1)]

    for x, y in pos:
        board[y-min_y][x-min_x] = '*'

    return [''.join(b) for b in board][::-1]

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
# print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution(line))