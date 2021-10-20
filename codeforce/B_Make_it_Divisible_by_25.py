import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

T = int(input())


def solve(n):
    if len(n) == 0:
        return 0
    if int(n) % 25 == 0:
        return 0

    if cache[n] != 0:
        return cache[n]

    ss = list(n)

    cache[n] = 987654321

    if ss[-1] != '0' and ss[-1] != '5':
        tmp = ss[-1]
        ss[-1] = ''
        cache[n] = min(cache[n], solve(''.join(ss)))
        ss[-1] = tmp
    else:
        tmp = ss[-1]

        ss[-1] = tmp


    return cache[n]


while T:
    ss = input()
    cache = defaultdict(int)
    print(solve(ss))

    T -= 1