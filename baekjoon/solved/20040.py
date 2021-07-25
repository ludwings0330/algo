import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
rank = [1 for _ in range(n+1)]

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

for i in range(1, m+1):
    x, y = map(int , input().split())
    if not union(x, y):
        print(i)
        break
else:
    print(0)