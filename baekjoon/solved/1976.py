#여행 가자
import sys
input = sys.stdin.readline

N = int(input()) # 도시의 수
M = int(input()) # 여행 계획에 속한 도시들의 수
trunk = [] # N*N 1 이면 연결 0 이면 연결 x
parent = [i for i in range(N)]
rank = [1] * N
def find(x):
    if parent[x] == x:
        return x
    y = find(parent[x])
    parent[x] = y
    return y
def union(x, y):
    x = find(x)
    y = find(y)
    if x == y: # 같은 부모!
        return
    if rank[x] > rank[y]:
        parent[y] = x
        rank[x] += rank[y]
    else:
        parent[x] = y
        rank[y] += rank[x]
def check(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return True
    else:
        return False

for i in range(N):
    line = list(map(int,input().split()))
    for j in range(len(line)):
        if line[j] == 1: # 연결되어 있다면 같은 집합
            union(i, j)
    trunk.append(line)

plan = list(map(int, input().split()))
for i in range(len(plan)):
    plan[i] -= 1

ans = True
for i in range(len(plan)-1):
    if not check(plan[i], plan[i+1]):
        ans = False
        break
if ans:
    print('YES')
else:
    print('NO')