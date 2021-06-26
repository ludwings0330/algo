import sys
import heapq

input = sys.stdin.readline

N = int(input())
hq = []
while N:
    N -= 1

    c = int(input())
    if c == 0:
        if hq:
            ans = heapq.heappop(hq)
            print(ans[0]*ans[1])
        else:
            print(0)
    else:
        if c < 0:
            heapq.heappush(hq, [-c, -1])
        else:
            heapq.heappush(hq, [c, 1])
