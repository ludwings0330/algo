import sys
input = lambda: sys.stdin.readline().rstrip()

TC = int(input())

while TC:
    TC -= 1

    x, y = map(int, input().split())
    dist = y-x

    k = 1
    while k**2 <= dist:
        k += 1
    k -= 1
    ans = k*2 - 1
    if dist - k ** 2 > k:
        ans += 2
    elif dist - k ** 2 > 0:
        ans += 1

    print(ans)