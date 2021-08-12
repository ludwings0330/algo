# title ; parcel
# tag ; 다이나믹 프로그래밍

import sys
input = lambda: sys.stdin.readline().rstrip()

w, n = map(int, input().split())
weights = list(map(int, input().split()))

weights.sort()
SUM = sum(weights[:4])

ans = [0, 1, 2, 3, n]
isAnswer = True if SUM == w else False

for i in range(3, -1, -1):
    for idx in range(ans[i] + 1, ans[i + 1]):
        if SUM < w:

            SUM -= weights[idx - 1]
            SUM += weights[idx]
            ans[i] = idx

            if SUM > w:
                SUM -= weights[idx]
                SUM += weights[idx - 1]
                ans[i] = idx-1
                break
        if SUM == w: # NO 인걸 True 라고 할 수는 없는구조.. 문제는 True 인걸 no 라고 해서 생긴다.
            isAnswer = True
            break
    if isAnswer or SUM > w:
        break
# print(ans)
print('YES' if isAnswer else 'NO')