# 서로가 서로를 갈 수 있는 노드들끼리 합

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
    # 이미 방문했다면 리턴
    if ID[node] != -1:
        return ID[node]

    # 방문 순서대로 고유한 id를 부여함으로 방문 여부와 부모를 check
    global IDID
    ID[node] = IDID
    IDID += 1

    # parent 는 node가 아니라 node의 ID를 가지고 있음을 기억
    parent = ID[node]
    stack.append(node)
    if node in graph:
        for next in graph[node]:
            if ID[next] == -1: # 아직 방문을 안했을 때
                parent = min(parent, get_ssc(next))
            elif not finished[next]: # 방문은 했지만 scc가 결정되지 않았을 때
                # 나하고 다음 거 중에 작은 id를 고른다
                parent = min(parent, ID[next])

    # 부모가 자기 자신일 경우 루프가 만들어지니까 scc 생성
    if parent == ID[node]:
        tmp = []
        while stack:
            n = stack.pop()
            tmp.append(n)
            finished[n] = True
            if n == node: #
                break
        scc_list.append(sorted(tmp))

    # return parent를 해줘야 dfs 완성
    return parent

for i in range(1, N+1):
    if ID[i] == -1:
        get_ssc(i)


print(len(scc_list))
for scc in sorted(scc_list):
    scc += [-1]
    print(*scc)

