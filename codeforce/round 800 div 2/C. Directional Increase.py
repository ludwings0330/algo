import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    l, r = 0, n - 1

    for i in range(1, n):
        a[i] += a[i-1]

    ans = True
    if a[-1] != 0:
        ans = False

    visited_zero = False
    for i in range(n):
        if a[i] < 0:
            ans = False
            break
        if a[i] == 0:
            visited_zero = True
        elif visited_zero:
            ans = False


    print('YES' if ans else 'NO')