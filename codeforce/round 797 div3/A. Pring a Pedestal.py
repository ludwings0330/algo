import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n = int(input())

    h1 = 2
    h2 = 1
    h3 = 0
    n -= 3
    while n > 0:
        h1 += 1
        n -= 1
        if not n:
            break
        h2 += 1
        n -= 1
        if not n:
            break
        h3 += 1
        n -= 1

    print(h2, h1, h3)
