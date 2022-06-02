import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n = int(input())
    p = list(map(int, input().split()))
    i = 0

    count = 0
    while i < n - 1:
        if p[i] > p[i+1]:
            count += 1
            i += 2
        else:
            i += 1
    print(count)