N = int(input())
board = [[0] * 1001 for _ in range(1001)]

for i in range(N):
    bt_left_x, bt_left_y, w, h = map(int, input().split())
    for x in range(bt_left_x, bt_left_x + w):
        for y in range(bt_left_y, bt_left_y + h):
            board[y][x] = i + 1

for i in range(N):
    area = 0
    for r in range(1001):
        for c in range(1001):
            if board[r][c] == i + 1:
                area += 1
    print(area)