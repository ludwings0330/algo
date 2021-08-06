# Title : 피리 부는 사나이
# Tag : 분리 집합

import sys
input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())

move = { 'D':(1, 0), 'L':(0, -1), 'R':(0, 1), 'U':(-1, 0)}

parent = [i for i in range(R*C)]
rank = [1 for _ in range(R*C)]

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

    if x == y:
        return False
    if rank[x] > rank[y]:
        parent[y] = x
        rank[x] += rank[y]
    else:
        parent[x] = y
        rank[y] += rank[x]
    return True
board = [list(input()) for _ in range(R)]
vis = [[False]*C for _ in range(R)]
ans = 0
for idx in range(R*C):
    r = idx // C
    c = idx % C
    if not vis[r][c]:
        vis[r][c] = True

        tr = r + move[board[r][c]][0]
        tc = c + move[board[r][c]][1]
        nidx = tr*C + tc
        if not union(idx, nidx): # 합치기 실패하면 roop 라는 뜻
            ans += 1
# print(parent)
print(ans)
