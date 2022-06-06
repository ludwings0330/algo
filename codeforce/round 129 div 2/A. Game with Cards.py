import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

while t:
    t -= 1

    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    a.sort()
    b.sort()
    if a[-1] > b[-1]:
        print('Alice')
        print('Alice')
    elif b[-1] > a[-1]:
        print('Bob')
        print('Bob')
    else:
        print('Alice')
        print('Bob')