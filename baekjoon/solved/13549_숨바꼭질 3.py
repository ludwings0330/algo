from collections import deque
# 메모리 초과가 나니까 ... 다시해

N, K = map(int, input().split())
MAX = 100005
visit = [False]*(MAX+1)

def BFS(N):
    dq = deque()
    dq.append([N, 0])
    ret = 0
    while dq:
        n, time = dq.popleft()
        visit[n] = True

        if n == K:
            ret = time
            break
        if n * 2 <= MAX:
            if not visit[n*2]:
                dq.append([n*2, time])
        if n + 1 <= MAX:
            if not visit[n+1]:
                dq.append([n+1, time+1])
        if n - 1 >= 0:
            if not visit[n - 1]:
                dq.append([n-1, time + 1])

    return ret
print(BFS(N))