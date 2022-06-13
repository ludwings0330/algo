import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n = int(input())

    h1 = h2 = h3 = n // 3
    if n % 3 == 0:
        h1 += 1
        h3 -= 1
    elif n % 3 == 1:
        h1 += 2
        h3 -= 1
    else:
        h1 += 2
        h2 += 1
        h3 -= 1

    print(h2, h1, h3)
