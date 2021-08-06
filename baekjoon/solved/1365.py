# Title : 꼬인 전깃줄
# Tag : LIS

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
pole = list(map(int, input().split()))
LIS = [pole[0]]

def lower_bound(x):
    left = 0
    right = len(LIS)

    while left < right:
        mid = (left + right)//2

        if LIS[mid] < x:
            left = mid + 1
        else:
            right = mid

    return right

for i in range(1, len(pole)):
    if LIS[-1] < pole[i]:
        LIS.append(pole[i])
    else:
        idx = lower_bound(pole[i])
        LIS[idx] = pole[i]
print(N - len(LIS))
