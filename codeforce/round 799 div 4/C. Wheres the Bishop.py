import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    input()
    board = [list(input()) for _ in range(8)]
    move = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    flag = True

    for r in range(1, 8):
        for c in range(1, 8):
            flag = True
            for tr, tc in move:
                nr = r + tr
                nc = c + tc
                if 0 <= nr < 8 and 0 <= nc < 8:
                    if board[nr][nc] != '#':
                        flag = False
                        break
            if flag:
                print(r+1, c+1)
                break
        if flag:
            break
