import sys
input = lambda: sys.stdin.readline().rstrip()
t = int(input())

while t:
    t -= 1
    n = int(input())
    board = list(input())

    result = True

    if n == 1 and board[0] != 'W':
        result = False
    elif n == 2 and ''.join(board) not in ["RB", "BR", "WW"]:
        result = False

    checker = ''
    isOk = True

    for ch in board:
        if ch == 'W':
            if not isOk:
                result = False
                break
            checker = ''
        else:
            if checker == '':
                checker = ch
                isOk = False
            else:
                if checker != ch:
                    isOk = True

    result = result and isOk

    print("YES" if result else "NO")