import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, k = map(int, input().split())
A = [0] + list(map(int, input().split()))


graph = {}
rank = [1] * (N+1)
parent = [i for i in range(N+1)]

def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return 0

    if rank[x] > rank[y]: # x의 자식이 더 많으니, y가 x 아래로 드간다.
        parent[y] = x
        rank[x] += rank[y]
        if A[x] > A[y]:
            A[x] = A[y]
        A[y] = 0
    else:
        parent[x] = y
        rank[y] += rank[x]

        if A[y] > A[x]:
            A[y] = A[x]
        A[x] = 0

    return 1

for _ in range(M):
    s, e = map(int, input().split())
    union(s, e)

total_price = sum(A)
if k >= total_price:
    print(total_price)
else:
    print('Oh no')
