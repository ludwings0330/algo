'''
1km 가는데, 1L의 연료가 샌다.

주유소에서 멈추는 횟소를 최소화

최소화 하려면 연료를 많이 주는 곳을 우선으로 들려야한다?


1. 마을까지 못간다면
2. 내가 갈 수 있는 거리에 있는 정류소 모두 heapq 에 저장
3. heapq에 있는 값중 제일 많은 연료를 주는 곳에서 주유
4. 최대 도착거리 갱신
5. 1~4번 반복

'''

import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

N = int(input())

# a, b
# a : 주유소의 x 좌표,
# b : 주유소에서 채울 수 있는 연료의 양
stations = []

for _ in range(N):
    stations.append(list(map(int, input().split())))
stations.sort()
L, P = map(int, input().split())

station = 0
current = P
ans = 0
hq = []

while True:
    if current >= L:
        break
    else:
        # 마을까지 못간다면, 내가 갈 수 있는 거리에 있는 모든 종류소 heapq에 저장.
        while station < N:
            if stations[station][0] > current:
                # 해당 정류소에 도달할 수 없으면 break
                break
            # 도달할 수 있는 모든 정류소 기름 순으로 저장
            heapq.heappush(hq, -stations[station][1])
            station += 1

        if not hq:
            break
        current += -heapq.heappop(hq)
        ans += 1

if current < L:
    print(-1)
else:
    print(ans)
