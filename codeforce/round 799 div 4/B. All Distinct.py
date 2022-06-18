import sys
input = lambda: sys.stdin.readline().rstrip()
t = int(input())
while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    store = set()

    for ai in a:
        store.add(ai)

    if (n - len(store)) % 2 == 0:
        print(len(store))
    else:
        print(len(store)-1)
