# 세 용액
# 알칼리 용액 < 0
# 산성 용액 > 0
# 세가지 용액을 혼합하여 특성 값이 0에 가장 가까운 용액 만들기.

import sys
input = sys.stdin.readline

N = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

MIN = sys.maxsize
ret = []
for i in range(N):
    left = 0
    right = N-1
    mid = i
    while left < right:
        if left == mid:
            left += 1
        if right == mid:
            right -= 1
        if left == right:
            break
        SUM = liquids[left] + liquids[mid] + liquids[right]

        if abs(SUM) < MIN:
            MIN = abs(SUM)
            ret = [liquids[left], liquids[mid], liquids[right]]
        if SUM < 0:
            left += 1
        elif SUM > 0:
            right -= 1
        else:
            break

print(*sorted(ret))