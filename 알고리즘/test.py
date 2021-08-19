import sys
input = lambda: sys.stdin.readline().rstrip()

graph = {}
N, M = map(int, input().split())

ID = [-1] * (N+1)
IDID = 1

scc_list = []
stack = []
finished = [False] * (N+1)

# get input
for _ in range(M):
    s, e = map(int, input().split())
    if s in graph:
        graph[s][e] = 1
    else:
        graph[s] = {e:1}

def get_ssc(node):
    if ID[node] != -1:
        return ID[node]

    global IDID
    ID[node] = IDID
    IDID += 1

    parent = ID[node]
    stack.append(node)
    if node in graph:
        for next in graph[node]:
            if ID[next] == -1: # 아직 방문을 안했을 때
                parent = min(parent, get_ssc(next))
            elif not finished[next]: # 방문은 했지만 scc가 결정되지 않았을 때
                parent = min(parent, ID[next])

    if parent == ID[node]:
        tmp = []
        while stack:
            n = stack.pop()
            tmp.append(n)
            finished[n] = True
            if n == node:
                break
        scc_list.append(sorted(tmp))

    return parent

for i in range(1, N+1):
    if ID[i] == -1:
        get_ssc(i)


print(len(scc_list))
for scc in sorted(scc_list):
    scc += [-1]
    print(*scc)

