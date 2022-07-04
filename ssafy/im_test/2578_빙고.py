board = [list(map(int, input().split())) for _ in range(5)]

pick = []
for _ in range(5):
    pick.extend(list(map(int, input().split())))

bingo = 0
for i in range(len(pick)):
    cr, cc = -1, -1

    for r in range(5):
        for c in range(5):
            if board[r][c] == pick[i]:
                board[r][c] = -1
                cr = r
                cc = c
                break
        if cr != -1:
            break

    for r in range(5):
        if board[r][cc] != -1:
            break
        elif board[r][cc] == -1 and r == 4:
            bingo += 1
    for c in range(5):
        if board[cr][c] != -1:
            break
        elif board[cr][c] == -1 and c == 4:
            bingo += 1

    if cr == cc:
        for k in range(5):
            if board[k][k] != -1:
                break
            elif board[k][k] == -1 and k == 4:
                bingo += 1
    if cr + cc == 4:
        for k in range(5):
            if board[k][4-k] != -1:
                break
            elif board[k][4-k] == -1 and k == 4:
                bingo +=1

    if bingo >= 3:
        print(i+1)
        break
