import sys
input = lambda:sys.stdin.readline().rstrip()

def find(x):
    if parent[x] == x:
        return x

    y = find(parent[x])
    parent[x] = y

    return y

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return 0

    if rank[x] > rank[y]:
        parent[y] = x
        rank[x] += rank[y]

    else:
        parent[x] = y
        rank[y] += rank[x]

    return 1

N, M, K = map(int,input().split())
parent = [i for i in range(N+1)]
rank = [1 for _ in range(N+1)]

graph = []

for i in range(1, M+1):


    s, e = map(int, input().split())
    if i == K:
        continue

    union(s, e)

cnt = 0
for i in range(1, N+1):
    if find(1) == find(i):
        cnt += 1

print(cnt*(N-cnt))