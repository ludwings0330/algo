import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    total = sum(a)
    flag = False

    for i in range(1, n - 1):
        if (total - a[i]) / (n - 1) == a[i]:
            flag = True
            break

    print('YES' if flag else 'NO')
