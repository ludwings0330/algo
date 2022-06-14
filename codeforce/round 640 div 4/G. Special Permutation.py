import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n = int(input())
    even = [i for i in range(2, n+1, 2)]
    odd = [i for i in range(1, n+1, 2)]
    odd.reverse()

    ans = odd

    if n < 3:
        print(-1)
    else:
        even[0], even[1] = even[1], even[0]
        ans += even
        print(*ans)
