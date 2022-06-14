import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
plus = []
minus = []

for _ in range(n):
    x, y = map(int, input().split())
    plus.append(x+y)
    minus.append(x-y)

plus.sort()
minus.sort()


def maximum_distance():
    return max(plus[-1] - plus[0], minus[-1] - minus[0])


def minimum_distance():
    ret = float('inf')

    for i in range(n):
        ret = min(ret, min(plus[i+1] - plus[i], minus[i+1] - minus[i]))

    return ret


print(maximum_distance())
