import sys
input = sys.stdin.readline

N = int(input())
MAP = []

for _ in range(N):
    line = list(input().rstrip())
    line = list(map(int, line))
    MAP.append(line)

ans = []
def check(sx, sy, ex, ey):
    flag = MAP[sy][sx]

    for i in range(sy, ey):
        for j in range(sx, ex):
            if MAP[i][j] != flag:
                return False
    return True

def divide(sx, sy, ex, ey):

    tx = sx + (ex - sx)//2
    ty = sy + (ey - sy)//2
    # 왼쪽위
    if check(sx, sy, ex, ey):
        ans.append(MAP[sy][sx])
    else:
        ans.append('(')

        if check(sx, sy, tx, ty):
            ans.append(MAP[sy][sx])
        else:
            divide(sx, sy, tx, ty)
        # 오른쪽 위
        if check(tx, sy, ex, ty):
            ans.append(MAP[sy][tx])
        else:
            divide(tx, sy, ex, ty)
        # 왼쪽아래
        if check(sx, ty, tx, ey):
            ans.append(MAP[ty][sx])
        else:
            divide(sx, ty, tx, ey)
        # 오른쪽아래
        if check(tx, ty, ex, ey):
            ans.append(MAP[ty][tx])
        else:
            divide(tx, ty, ex, ey)
        ans.append(')')
divide(0, 0, N, N)
print(*ans, sep='')