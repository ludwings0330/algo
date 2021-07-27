# Title : 공항
# 최대한 많은 수의 비행기 도킹하기
import sys
input = lambda: sys.stdin.readline().rstrip()

G = int(input())
P = int(input())
g = []

parent = [i for i in range(G+1)]
rank = [1] * (G+1)

def find(x):
    if x == parent[x]:
        return x
    else:
        y = find(parent[x])
        parent[x] = y  # x 의 부모를 바꿔주는 과정으로 효율 UP
        return y

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False

    parent[y] = x
    return True

for _ in range(P):
    g.append(int(input()))

cnt = 0
for gi in g:
    idx = find(gi)
    if idx == 0:
        break
    else:
        cnt += 1
        union(idx-1, idx)

print(cnt)