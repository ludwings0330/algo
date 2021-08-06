import sys
input = sys.stdin.readline
from collections import deque

VISIT = [sys.maxsize]*100001
ans = {} # 시간 : 갯수

N, K = map(int, input().split())

dq = deque()
dq.append([N, 0])
VISIT[N] = 0
ret = sys.maxsize

while dq:
    num, time = dq.popleft()

    if num == K:
        ret = min(ret, time)
        if time in ans:
            ans[time] += 1
        else:
            ans[time] = 1
    else:
        next = num * 2
        if next < 100001 and VISIT[next] > time:
            dq.append([next, time+1])
            VISIT[next] = time+1

        next = num +1
        if next < 100001 and VISIT[next] > time:
            dq.append([next, time + 1])
            VISIT[next] = time+1

        next = num - 1
        if 0 <= next and VISIT[next] > time:
            dq.append([next, time + 1])
            VISIT[next] = time+1

print(ret)
print(ans[ret])