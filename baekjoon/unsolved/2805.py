import sys
input = sys.stdin.readline

N, M = map(int,input().split())
trees = list(map(int, input().split()))

left = 0
right = 1000000000
mid = 0

MIN = sys.maxsize

while left <= right:
    mid = (right + left)//2
    m = 0
    for tree in trees:
        if tree > mid:
            m += tree-mid


    if m > M: # 너무 작게 잘랐으. 더 크게 ㄱㄱ
        left = mid + 1
    elif m <= M: # 너무 크게 잘았으. 더 작게 ㄱ
        right = mid - 1
        MIN = min(mid, MIN)

print(MIN)