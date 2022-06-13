import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict
sys.setrecursionlimit(10**5)

def dfs(current, parent):
    s = 0
    for child in graph[current]:
        if child != parent:
            dfs(child, current)
            s += dp[child]
            chs[current] += chs[child]

    for child in graph[current]:
        if child != parent:
            dp[current] = max(dp[current], s - dp[child] + chs[child] - 1)


t = int(input())
while t:
    t -= 1
    n = int(input())
    graph = defaultdict(lambda: defaultdict(int))

    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u][v] = graph[v][u] = True

    chs = [1] * (n+1)
    dp = [0] * (n+1)

    dfs(1, 0)
    print(dp[1])
