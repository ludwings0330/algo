import sys
from collections import defaultdict


input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    counter = defaultdict(int)

    result = 0

    for n in arr:
        counter[n] += 1
        if counter[n] >= 3:
            result = n
            break

    print(-1 if result==0 else result)