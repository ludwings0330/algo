import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n, k = map(int, input().split())

    odd = n-(k-1)
    even = n - (k - 1) * 2
    if odd > 0 and odd % 2 == 1:
        print('YES')
        print(*[1 for _ in range(k-1)], odd)
    elif even > 0 and even % 2 == 0:
        print('YES')
        print(*[2 for _ in range(k-1)], even)
    else:
        print('NO')


