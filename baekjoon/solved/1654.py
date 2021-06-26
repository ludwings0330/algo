import sys
input = sys.stdin.readline

K, N = map(int,input().split())
nums = []

for _ in range(K):
    num = int(input())
    nums.append(num)

left = 0
right = sys.maxsize
mid = 0
MAX = 0

while left <= right:
    mid = (right + left)//2
    n = 0
    for num in nums:
        n += num//mid


    if n >= N: # 너무 작게 쪼갬 더 크게
        left = mid + 1
        MAX = max(mid, MAX)
    else:
        right = mid - 1

print(MAX)