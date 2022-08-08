# 박스 N개, 서로다른 색상의 카드 M개
# 1개는 조커박스 모든 색상
# 다른박스들은 모두 같은색 혹은 비어있음
# 최소이동으로 위의조건 만족

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter

N, M = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(N)]

for box in boxes:
    counter = 0
    for card in box:
        if card != 0:
            counter += 1
    print(counter)
