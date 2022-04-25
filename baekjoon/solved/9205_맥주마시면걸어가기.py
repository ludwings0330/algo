# 최대 1000 미터
# 편의점에서 리필
# 페스티벌에 도착할 수 있는지 없는지
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

SUCCESS = "happy"
FAIL = "sad"

t = int(input())


def is_reachable(fr, to):
    x_dist = abs(fr[0] - to[0])
    y_dist = abs(fr[1] - to[1])
    total_dist = x_dist + y_dist

    return True if total_dist <= 1000 else False


for testCase in range(t):
    n = int(input())

    start_coord = list(map(int, input().split()))
    shops = []

    for i in range(n):
        shop_tmp = list(map(int, input().split()))
        shops.append(shop_tmp)

    end_coord = list(map(int, input().split()))
    shops.append(end_coord)

    visit = [False] * (len(shops))

    dq = deque()

    dq.append(start_coord)
    isSuccess = False

    while dq:
        current_coord = dq.popleft()
        if current_coord == end_coord:
            isSuccess = True
            break

        for i, shop in enumerate(shops):
            if not visit[i] and is_reachable(current_coord, shop):
                visit[i] = True
                dq.append(shop)

    print(SUCCESS if isSuccess else FAIL)
