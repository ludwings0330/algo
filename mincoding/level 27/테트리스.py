board = [list(map(int, input().split())) for _ in range(5)]
ans = []
for r in range(5):
    if sum(board[r]) == 4:
        ans.insert(0, [0, 0, 0, 0])
    else:
        ans.append(board[r])

for r in range(5):
    print(*ans[r])