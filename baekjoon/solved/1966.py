import sys
from collections import deque
import heapq

input = sys.stdin.readline

TC = int(input())

while TC:
    TC -= 1
    N, K = map(int, input().split()) # index K 가 궁그매
    dq = deque(list(map(int, input().split())))


    hq = []
    for i, v in enumerate(dq):
        heapq.heappush(hq, [-v, i])
    c = 0
    while dq:
        if dq[0] == -hq[0][0]:
            dq.popleft()
            v, i = heapq.heappop(hq)
            c += 1
            if i == K:
                break
        else:
            dq.append(dq.popleft())
    print(c)