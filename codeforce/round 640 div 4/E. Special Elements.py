import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

t = int(input())
while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    store = defaultdict(int)

    for el in a:
        store[el] += 1

    ans = 0
    for l in range(n-1):
        total = a[l]
        for r in range(l+1, n):
            total += a[r]
            if total <= n:
                ans += store[total]
                store[total] = 0

    print(ans)
