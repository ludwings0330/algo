import sys
input = sys.stdin.readline

N = int(input())
visit = [False] * (N+1)
trunk = {}
answer = [0] * (N+1)


for i in range(N-1):
    s, f = map(int, input().split())
    if s not in trunk:
        trunk[s] = [f]
    else:
        trunk[s].append(f)

    if f not in trunk:
        trunk[f] = [s]
    else:
        trunk[f].append(s)

def DFS():
    stack = []
    stack.append(1)
    answer[1] = 1
    visit[1] = True

    while stack:
        node = stack.pop()

        for i in range(len(trunk[node])):
            if not visit[trunk[node][i]]:
                # 방문하지 않았고, 간선이 존재한다면
                answer[trunk[node][i]] = node
                stack.append(trunk[node][i])
                visit[trunk[node][i]] = True

DFS()
print('\n'.join(str(_) for _ in answer[2:]))

