# Title ; 행성 터널
# Tag ; 정렬, 최소 스패닝 트리

import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())

x_list = []
y_list = []
z_list = []

for i in range(N):
    x, y, z = map(int, input().split())

    x_list.append([x, i])
    y_list.append([y, i])
    z_list.append([z, i])

x_list.sort()
y_list.sort()
z_list.sort()


xyz_list = []
for i in range(1, N):
    # x의 차이와 두 idx를 넣어준다.
    xyz_list.append([abs(x_list[i - 1][0] - x_list[i][0]), x_list[i - 1][1], x_list[i][1]])
    xyz_list.append([abs(y_list[i - 1][0] - y_list[i][0]), y_list[i - 1][1], y_list[i][1]])
    xyz_list.append([abs(z_list[i - 1][0] - z_list[i][0]), z_list[i - 1][1], z_list[i][1]])

xyz_list.sort()

parent = [i for i in range(N+1)]
rank = [1 for i in range(N+1)]

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

ans = 0
c = 0
for node in xyz_list:
    value, i, j = node
    if union(i, j):
        ans += value
        c += 1
    if c == N:
        break

print(ans)