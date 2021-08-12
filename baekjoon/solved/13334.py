# title ; 철로
# tag ; 우선순위 큐

import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

n = int(input())
pos = []
MIN = sys.maxsize
for _ in range(n):
    s, e = map(int, input().split())
    if s > e:
        s, e = e, s
    MIN = min(MIN, s)
    pos.append([s, e])

d = int(input())


ans = 0
hq_start = []
hq_end = []
start = MIN
for i in range(n):
    if start <= pos[i][0] and pos[i][1] <= start + d:
        heapq.heappush(hq_start, [pos[i][0], pos[i]])
    else:
        heapq.heappush(hq_end, [pos[i][1], pos[i]])

# start point를 움직인다.
# 큐 앞의 시작점이 pos[0][0] < start 가 되어 있다면 범위를 벗어났으므로 제외 해야한다. ( 제외가 되지 않을때까지 반복 )
# end point 확인, 새로운 끝점이 들어오면 시작점이 범위 내에 있는지 확인하고 범위 안이면 heap에 추가해준다.
ans = len(hq_start)

while hq_end:
    start += 1
    end = start + d

    while hq_start and hq_start[0][0] < start: # 범위 안에 없다면 버려준ㅗㅂ
        heapq.heappop(hq_start)

    while hq_end and hq_end[0][0] <= end:
        t, node = heapq.heappop(hq_end)
        if start <= node[0]:
            heapq.heappush(hq_start, [node[0], node])

    ans = max(ans, len(hq_start))

print(ans)