# Title ; 벡터 매칭
# Tag : 브루트 포스

import sys
input = lambda: sys.stdin.readline().rstrip()

TC = int(input())

def recursive_solve(idx, toPick, ix_sum, iy_sum):
    if toPick == 0:
        global ans
        ans = min(((x_sum-ix_sum*2)**2+(y_sum-iy_sum*2)**2)**(1/2), ans)
        return

    if idx == N:
        return

    for i in range(idx+1, N):
        recursive_solve(i, toPick -1, ix_sum + x_list[i], iy_sum + y_list[i])

while TC:
    TC -= 1

    N = int(input())

    x_list = []
    y_list = []
    for _ in range(N):
        x, y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)

    x_sum = sum(x_list)
    y_sum = sum(y_list)

    ans = sys.maxsize

    recursive_solve(-1, N//2, 0, 0)
    print(ans)