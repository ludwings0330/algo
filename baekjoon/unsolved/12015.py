# # 가장 긴 증가하는 부분 수열 2
# import sys
# from bisect import bisect_left
#
# # import random
# input = sys.stdin.readline
#
# N = int(input())
# arr = list(map(int, input().split()))
# # N = 1000000
# # arr = [random.randint(1,1000000) for i in range(N)]
# LIST = [0]
#
# for num in arr:
#     if LIST[-1] < num:
#         LIST.append(num)
#     else:
#         LIST[bisect_left(LIST, num)] = num
# print(len(LIST)-1)
# 가장 긴 증가하는 부분 수열 2

import sys
# import random
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
# N = 1000000
# arr = [random.randint(1,1000000) for i in range(N)]
LIST = [arr[0]]
LIS = 1

def bSearch(target):
    left = 0
    right = LIS-1
    while left <= right:
        mid = (left + right)//2
        if LIST[mid] == target:
            break
        elif LIST[mid] < target:
            left = mid+1
        elif LIST[mid] > target:
            right = mid-1
    if left > right: # 찾지 못했을 때,
        if mid == 0:
            if LIST[mid] > target:
                LIST[mid] = target
            elif LIST[mid] < target:
                LIST[right] = target
        else:
            pass
    else:
        LIST[mid] = target

for i in range(1, N):
    if LIST[-1] < arr[i]:
        LIST.append(arr[i])
        LIS += 1
    else:
        bSearch(arr[i])
print(LIST)
print(LIS)
