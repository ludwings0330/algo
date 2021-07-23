import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

TC = int(input())
move = ((0, 1), (0, -1), (1, 0), (-1, 0))

while TC:
    TC -= 1
    h, w = map(int , input().split())

    board = [['.']*(w+2)]
    for _ in range(h):
        line = list(input())
        board.append(['.'] + line + ['.'])
    board.append(['.']*(w+2))
    keys = set(list(input()))

    ans = 0
    newKey = True
    while newKey:
        newKey = False
        dq = deque()
        visit = set()
        dq.append((0, 0))
        visit.add((0, 0))

        while dq:
            x, y = dq.popleft()

            for i in range(4):
                tx = x + move[i][0]
                ty = y + move[i][1]

                if 0 <= tx < w+2 and 0 <= ty < h+2 and board[ty][tx] != '*' and (tx, ty) not in visit:
                    if board[ty][tx].isupper(): # 문이다
                        if board[ty][tx].lower() not in keys:
                            continue
                    elif board[ty][tx].islower(): # 열쇠다.
                        if board[ty][tx] not in keys: # 새로운 열쇠다.
                            newKey = True
                            keys.add(board[ty][tx])
                        else: # 이미 있는 열쇠면 무시
                            pass
                    elif board[ty][tx] == '$': # 문서다
                        ans += 1
                        board[ty][tx] = '.'

                    dq.append((tx, ty))
                    visit.add((tx, ty))
    print(ans)