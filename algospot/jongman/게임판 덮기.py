dx = [[0, 1, 0], [0, 0, -1], [0, 1, 1], [0, 0, 1]]
dy = [[0, 0, 1], [0, 1, 1], [0, 0, 1], [0, 1, 1]]

CHECK = 1
FILL = -1
DEL = 0
def checkMode(x, y, m, k):
    if k == CHECK:
        for i in range(3):
            if 0 > y + dy[m][i] or y + dy[m][i] >= H or 0 > x + dx[m][i] or x + dx[m][i] >= W:
                return False
            elif gameBoard[y + dy[m][i]][x + dx[m][i]] != '.':
                return False

    elif k == DEL: # 삭제
        for i in range(3):
            gameBoard[y + dy[m][i]][x + dx[m][i]] = '.'
    else: # k == 0 # 추가
        for i in range(3):
            gameBoard[y + dy[m][i]][x + dx[m][i]] = '#'

    return True

def recursiveSolve(ny):
    finished = True
    tx, ty = -1, -1 # x, y

    for i in range(ny, H):
        if not finished:
            break
        for j in range(W):
            if gameBoard[i][j] == '.':
                tx, ty = j, i
                finished = False
                break

    if finished:
        return 1

    ret = 0

    for i in range(4): #들어갈수 있는 방법이 4개다.
        if checkMode(tx, ty, i, CHECK):
            checkMode(tx, ty, i, FILL)
            ret += recursiveSolve(ty)
            checkMode(tx, ty, i, DEL)

    return ret


if __name__ == "__main__":
    C = int(input())

    while C:
        C -= 1
        H, W = map(int, input().split())
        gameBoard = []

        for i in range(H):
            line = list(input().rstrip())
            gameBoard.append(line)

        print(recursiveSolve(0))