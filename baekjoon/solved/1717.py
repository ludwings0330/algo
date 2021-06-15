# 집합의 표현
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

rank = [1] * (n+1)
parent = [i for i in range(n+1)]
def find(x):
    if parent[x] == x:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y
    pass
def union(x, y, command):
    x = find(x)
    y = find(y)
    if x == y:
        return True
    if command == 0:
        if rank[x] > rank[y]:
            parent[y] = x
            rank[x] += rank[y]
        else:
            parent[x] = y
            rank[y] += rank[x]
    return False

while m:
    m -= 1
    command, a, b = map(int, input().split())

    if command == 0: # a, b 합집합만들기
        union(a, b, command)

    elif command ==1: # a, b 가 같은 집합?
        if union(a, b, command):
            print('YES')
        else:
            print("NO")
