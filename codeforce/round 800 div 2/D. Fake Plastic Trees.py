import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict
sys.setrecursionlimit(10**5 + 50)

def dfs(i):
    total = 0
    for nxt in graph[i]:
        total += dfs(nxt)
    if total < l[i]:
        global ans
        ans += 1
        return r[i]

    return min(total, r[i])


t = int(input())
while t:
    t -= 1
    n = int(input())

    p = [0, 0] + list(map(int, input().split()))
    graph = defaultdict(list)
    for i in range(len(p)):
        graph[p[i]].append(i)

    l = [0]
    r = [0]
    for _ in range(n):
        ll, rr = map(int, input().split())
        l.append(ll)
        r.append(rr)

    ans = 0
    dfs(1)
    print(ans)
