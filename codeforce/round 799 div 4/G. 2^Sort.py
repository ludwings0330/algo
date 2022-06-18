import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    ok = []
    for i in range(n-1):
        if a[i] < a[i+1] * 2:
            ok.append(1)
        else:
            ok.append(0)

    total = sum(ok[0:k])
    if total == k:
        ans += 1

    for i in range(k, n-1):
        total += ok[i]
        total -= ok[i-k]
        if total == k:
            ans += 1

    print(ans)
