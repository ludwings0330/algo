import sys
input = sys.stdin.readline

row = [[0]*9 for _ in range(9)]
col = [[0]*9 for _ in range(9)]
square = [[[0]*9 for _ in range(3)] for __ in range(3)]
MAP = []
for _ in range(9):
    MAP.append(list(map(int, list(input().rstrip()))))
count = 0
for i in range(9):
    for j in range(9):
        if MAP[i][j] != 0:
            row[i][MAP[i][j]-1] = 1
            col[j][MAP[i][j]-1] = 1
            square[i//3][j//3][MAP[i][j]-1] = 1
        else:
            count += 1 # 빈자리 센다.

def solve(r, remain):
    if remain == 0:
        for l in MAP:
            print(*l,sep='')
        return 1

    ret = -1


    for i in range(9):
        for j in range(9):
            if MAP[i][j] == 0:
                noAns = True
                for k in range(9):
                    if row[i][k] == 0 and col[j][k] == 0 and square[i//3][j//3][k] == 0:
                        noAns = False
                        MAP[i][j] = k+1
                        row[i][k] = 1
                        col[j][k] = 1
                        square[i // 3][j // 3][k] = 1
                        ret = solve(i, remain-1)
                        if ret == 2: # 이새끼 때문에 반복 도는 거였어.
                            noAns = True
                        elif ret == 1:
                            return ret
                        MAP[i][j] = 0
                        row[i][k] = 0
                        col[j][k] = 0
                        square[i // 3][j // 3][k] = 0
                if noAns:
                    return 2
    return ret
solve(0, count)

