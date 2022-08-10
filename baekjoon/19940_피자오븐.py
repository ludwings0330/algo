import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

while T:
    T -= 1
    N = int(input())
    ans = [0, 0, 0, 0, 0]
    ans[0] = N//60
    N %= 60
    if N//10 <= 3:
        ans[1] = N//10
    else:
        ans[0] += 1
        ans[2] = 6 - N//10
    N %= 10
    if N <= 5:
        ans[3] = N
    else:
        ans[1] += 1
        ans[4] = 10 - N
    if ans[1] > 0 and ans[2] > 0:
        gap = abs(ans[1] - ans[2])
        ans[1] -= ans[1] - gap
        ans[2] -= ans[2] - gap

    print(*ans)