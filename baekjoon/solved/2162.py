# Title : 선분 그룹
# Tag : CCW, union find
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
parent = [i for i in range(N)]
rank = [1 for _ in range(N)]

lines = [list(map(int, input().split())) for _ in range(N)]
# [x1, y1, x2, y2]

def isIntersect(line_A, line_B):
    point_A_1 = line_A[:2]
    point_A_2 = line_A[2:]

    point_B_1 = line_B[:2]
    point_B_2 = line_B[2:]

    r1 = CCW(point_A_1, point_A_2, point_B_1)
    r2 = CCW(point_A_1, point_A_2, point_B_2)
    r3 = CCW(point_B_1, point_B_2, point_A_1)
    r4 = CCW(point_B_1, point_B_2, point_A_2)
    if r1*r2 == 0 and r3*r4 == 0:
        if point_A_1 > point_A_2:
            point_A_1, point_A_2 = point_A_2, point_A_1
        if point_B_1 > point_B_2:
            point_B_1, point_B_2 = point_B_2, point_B_1
        return (point_A_1 <= point_B_2) and (point_B_1 <= point_A_2)

    return r1*r2 <= 0 and r3*r4 <= 0

def CCW(a, b, c):
    return (a[0]*b[1]+b[0]*c[1]+c[0]*a[1])-(a[1]*b[0]+b[1]*c[0]+c[1]*a[0])
def find(x):
    if x == parent[x]:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y
def union(x, y):
    x = find(x)
    y = find(y)

    if x == y: # 같은 부모면 return
        return False

    if rank[x] > rank[y]:
        parent[y] = x
        rank[x] += rank[y]
    else:
        parent[x] = y
        rank[y] += rank[x]
    return True
nGroup = 0
for i in range(N):
    for j in range(i+1, N):
        if isIntersect(lines[i], lines[j]): # 겹치면 연결
            union(i, j)
ans = set()
for i in range(N):
    ans.add(find(i))
print(len(ans))
print(max(rank))
