import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n = int(input())
MAX = 0
graph = {}
visit = [False] * (n+1)

for i in range(n):
    line = list(map(int, input().split()))
    graph[line[0]] = {line[1]:line[2]}
    for j in range(3, len(line)-1, 2):
        graph[line[0]][line[j]] = line[j+1]
MAX = 0
def recursiveSolve(node):
    if node not in graph:
        return 0

    ret = 0
    length = [0] * len(graph[node])
    for i, next  in enumerate(graph[node]):
        if not visit[next]:
            visit[next] = True
            length[i] = graph[node][next] + recursiveSolve(next)
            visit[next] = False
    global MAX
    length.sort()
    if node == 1:
        lengthindex = [i for i in graph[node]]
        index = length.index(length[-1])
    MAX = max(MAX, sum(length[-2:]))
    return max(length)
index = -1
visit[1] = True
recursiveSolve(1)
visit[1] = False
visit[index] = True
recursiveSolve(index)

print(MAX)