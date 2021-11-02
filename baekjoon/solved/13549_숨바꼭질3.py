from collections import deque

def BFS(N):
    dq = deque()
    dq.append([N, 0])
    ret = float('inf')
    while dq:
        n, time = dq.popleft()
        visit[n] = True
        if n == K:
            ret = min(ret, time)
        if n * 2 < MAX and not visit[n * 2]:
            dq.append([n * 2, time])
        if n + 1 < MAX and not visit[n + 1]:
            dq.append([n + 1, time + 1])
        if n - 1 >= 0 and not visit[n - 1]:
            dq.append([n - 1, time + 1])

    return ret


MAX = 100001
N, K = map(int, input().split())
visit = [False] * (MAX)
array = [0] * MAX

print(BFS(N))