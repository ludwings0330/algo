import sys
input = sys.stdin.readline

N, M , y, x, k = map(int, input().split())
MAP = [list(map(int,input().split())) for _ in range(N)]
command = list(map(int, input().rstrip().split()))
# 1 : 동, 2 : 서, 3 : 북, 4 : 남
# 4 2 0 0 8
# 0 2
# 3 4
# 5 6
# 7 8
# 4 4 4 1 3 3 3 2
face = 0
right = 0
left = 0
top = 0
bottom = 0
back = 0

dd = ((0, 0), (1, 0), (-1, 0), (0, -1), (0, 1))
def rotate(d):
    global face, right, left, top, bottom, back
    if d == 1:
        face, right, back, left = left, face, right, back
        pass
    elif d == 2:
        face, left, back, right = right, face, left, back
        pass
    elif d == 3:
        face, top, back, bottom = bottom, face, top, back
        pass
    elif d == 4:
        face, bottom, back, top = top, face, bottom, back
        pass

for d in command:
    if 0 <= x + dd[d][0] < M and 0 <= y + dd[d][1] < N:
        x += dd[d][0]
        y += dd[d][1]
        rotate(d)
        if MAP[y][x] == 0:
            MAP[y][x] = back
        else:
            back = MAP[y][x]
            MAP[y][x] = 0

        print(face)