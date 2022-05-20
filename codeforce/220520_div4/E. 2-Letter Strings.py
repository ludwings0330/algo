import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

t = int(input())

while t:
    t -= 1
    n = int(input())
    strings = [input() for _ in range(n)]

    forward = defaultdict(lambda: defaultdict(int))
    backward = defaultdict(lambda: defaultdict(int))

    result = 0
    for string in strings:
        fi, se = list(string)
        result += sum(forward[fi].values()) - forward[fi][se]
        result += sum(backward[se].values()) - backward[se][fi]

        forward[fi][se] += 1
        backward[se][fi] += 1

    print(result)