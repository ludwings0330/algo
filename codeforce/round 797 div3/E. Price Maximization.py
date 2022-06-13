import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n, k = map(int, input().split())
    goods = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans += goods[i] // k
        goods[i] = goods[i] % k

    goods.sort()
    left = 0
    right = n - 1
    while left < right:
        if goods[left] + goods[right] >= k:
            left += 1
            right -= 1
            ans += 1
        elif goods[left] + goods[right] < k:
            left += 1
    print(ans)

