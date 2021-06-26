import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n = int(input())
MAX = 0
graph = {}

for i in range(n-1):
    s, e, v = map(int, input().split())
    if s in graph:
        graph[s][e] = v
    else:
        graph[s] = {e:v}

MAX = 0
def recursiveSolve(node):
    if node not in graph:
        return 0

    ret = 0
    length = [0] * len(graph[node])
    for i, next  in enumerate(graph[node]):
        length[i] = graph[node][next] + recursiveSolve(next)

    global MAX
    length.sort()
    MAX = max(MAX, sum(length[-2:]))
    return max(length)
recursiveSolve(1)
print(MAX)