from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [False] * (F+1)
dq = deque()
dq.append((S, 0))
ans = -1
while dq:
    f, cnt = dq.popleft()

    if f <= 0 or f > F:
        continue

    if f == G:
        ans = cnt
        break

    if visited[f]:
        continue
    visited[f] = True

    dq.append((f+U, cnt + 1))
    dq.append((f-D, cnt + 1))

print(ans if ans != -1 else 'use the stairs')