import sys
input = lambda: sys.stdin.readline().rstrip()
t = int(input())
while t:
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))

    if n == 1:
        print(-1)
        continue

    ans = [i for i in range(1, n+1)]

    for i in range(n-1):
        if ans[i] == arr[i]:
            ans[i], ans[i+1] = ans[i+1], ans[i]
    if ans[-1] == arr[-1]:
        ans[-1], ans[-2] = ans[-2], ans[-1]

    print(*ans)
