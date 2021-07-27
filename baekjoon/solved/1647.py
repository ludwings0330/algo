import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

N, M = map(int, input().split())

parent = [i for i in range(N+1)]
rank = [1 for _ in range(N+1)]

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
        return False# 공통 분모니까 합치기 실행 안된다.

    # 높이가 더 낮은 트리를 높이가 높은 트리 밑에 넣는다.
    if rank[x] > rank[y]:
        parent[y] = x
        rank[x] += rank[y]
    else:
        parent[x] = y
        rank[y] += rank[x]

    return True # 공통 분모가 아니므로 합쳐진다링
hq = []
for i in range(M):
    A, B, C = map(int, input().split())
    heapq.heappush(hq, (C, A, B))

ans = 0
visit = set()
MAXC = -1
while hq:
    C, A, B = heapq.heappop(hq)
    if (A, B) in visit or not union(A, B): # 이미 방문했거나 사이클이 생긴다면
        continue
    # 방문하지 않았고, 싸이클이 생기지 않는다면 진행
    ans += C
    MAXC = max(MAXC, C)
    visit.add((A, B))
    visit.add((B, A))
print(ans-MAXC)