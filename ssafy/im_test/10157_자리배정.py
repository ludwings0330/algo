C, R = map(int, input().split())
K = int(input())

if C * R < K:
    print(0)
else:
    board = [[0] * R for _ in range(C)]
    tr = 0
    tc = 1

    cr, cc = 0, 0
    for i in range(1, C*R + 1):
        board[cr][cc] = i

        if tr != 0:
            if cr + tr == C or board[cr + tr][cc] != 0:
                if tr == 1:
                    tc = -1
                else:
                    tc = 1
                tr = 0

        elif tc != 0:
            if cc + tc == R or board[cr][cc + tc] != 0:
                if tc == 1:
                    tr = 1
                else:
                    tr = -1
                tc = 0
        cr += tr
        cc += tc

    flag = False
    for r in range(C):
        for c in range(R):
            if board[r][c] == K:
                print(r+1, c + 1)
                flag = True
                break
        if flag:
            break
