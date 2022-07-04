board = [[0] * 101 for _ in range(101)]

for _ in range(4):
    bt_left_x, bt_left_y, tp_right_x, tp_right_y = map(int, input().split())
    for x in range(bt_left_x, tp_right_x):
        for y in range(bt_left_y, tp_right_y):
            board[y][x] = 1

area = 0
for r in range(101):
    for c in range(101):
        area += board[r][c]

print(area)