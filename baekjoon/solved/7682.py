import sys
input = sys.stdin.readline

def check(inputString):
    ret = 0
    board = [[0]*3 for _ in range(3)]
    for i in range(9):
        board[i//3][i%3] = inputString[i]
    W = ''
    if board[0][0] != '.':
        if board[0][0] == board[0][1] == board[0][2]:
            W = board[0][0]
            ret += 1
        if board[0][0] == board[1][0] == board[2][0]:
            W = board[0][0]
            ret += 1
        if board[0][0] == board[1][1] == board[2][2]:
            W = board[0][0]
            ret += 1
    if board[1][1] != '.':
        if board[0][1] == board[1][1] == board[2][1]:
            W = board[1][1]
            ret += 1
        if board[1][1] == board[1][0] == board[1][2]:
            W = board[1][1]
            ret += 1
        if board[2][0] == board[1][1] == board[0][2]:
            W = board[1][1]
            ret += 1
    if board[2][2] != '.':
        if board[2][2] == board[2][1] == board[2][0]:
            W = board[2][2]
            ret += 1
        if board[2][2] == board[1][2] == board[0][2]:
            W = board[2][2]
            ret += 1
    return [ret, W]


while True:
    inputString = input().rstrip()
    if inputString == 'end':
        break
    bValid = True

    nO = inputString.count('O')
    nX = inputString.count('X')
    nD = inputString.count('.')
    if 0 <= nX - nO <= 1:
        pass
    else:
        bValid = False

    if bValid:
        [cnt, w] = check(inputString)
        if cnt >= 2:
            if nD == 0 and inputString[0] == inputString[2] == inputString[4] == inputString[6] == inputString[8]:
                pass
            else:
                bValid = False
        elif cnt == 0 and nD == 0:
            pass
        elif cnt == 1 and w == 'X': # X가 이겼을 때 같은 수면 안돼
            if nX == nO:
                bValid = False
        elif cnt == 1 and w == 'O': # O가 이겼을때 같은 수여야함
            if nX != nO:
                bValid = False
        elif cnt == 0:
            bValid = False
    # X 가 이겼을때, 같은수면 안돼
    # O 가 이겼을때, 같은수여야해
    if bValid:
        print('valid')
    else:
        print('invalid')


