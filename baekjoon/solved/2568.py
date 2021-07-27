# Title : 전깃줄 - 2
# Tag : LIS

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
pole = [list(map(int, input().split())) for _ in range(N)]
pole.sort()

LIS = [pole[0]]

def under_bound(target):
    left = 0
    right = len(LIS)

    while left < right:
        mid = (left+right)//2

        if LIS[mid][1] < target:
            left = mid + 1
        else:
            right = mid

    return right
stack = [[0, pole[0]]]
for i in range(1, N):
    if LIS[-1][1] > pole[i][1]:
        idx = under_bound(pole[i][1])
        LIS[idx] = pole[i]
        stack.append([idx, pole[i]])
    else:
        LIS.append(pole[i])
        stack.append([len(LIS)-1, pole[i]])

print(N - len(LIS))
ans = []
cnt = len(LIS)-1
for c in stack[::-1]:
    if cnt == c[0]:
        cnt -= 1
    else:
        ans.append(c[1][0])
ans.sort()
for a in ans:
    print(a)