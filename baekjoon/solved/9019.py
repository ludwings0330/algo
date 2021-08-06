import sys
from collections import deque

input = sys.stdin.readline
TC = int(input())

while TC:
    TC -= 1
    visit = [False] * 10000
    dq = deque()
    N, M = map(int, input().split())

    dq.append([N, ""])
    visit[N] = True

    while dq:
        num, ans = dq.popleft()
        if num == M:
            print(ans)
            break
        d = (num*2)%10000
        if not visit[d]:
            dq.append([d, ans+'D'])
            visit[d] = True

        s = num-1 if num!=0 else 9999
        if not visit[s]:
            dq.append([s, ans+'S'])
            visit[s] = True

        d = [0, 0, 0, 0]
        N = num
        for i in range(3, -1, -1):
            d[i] = N % 10
            N //= 10
        l = d[1] * 1000 + d[2] * 100 + d[3] * 10 + d[0]

        if not visit[l]:
            dq.append([l, ans+'L'])
            visit[l] = True

        d = [0, 0, 0, 0]
        N = num
        for i in range(3, -1, -1):
            d[i] = N % 10
            N //= 10
        r = d[3] * 1000 + d[0] * 100 + d[1] * 10 + d[2]

        if not visit[r]:
            visit[r] = True
            dq.append([r, ans+'R'])