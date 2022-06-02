import sys
input = lambda: sys.stdin.readline()
from collections import Counter

t = int(input())
while t:
    t -= 1
    n = int(input())
    s = list(map(int, input().split()))

    counter = Counter(s)

    is_possible = True

    for key in counter:
        if counter[key] == 1:
            is_possible = False
            break

    if is_possible:
        answer = []

        before = after = 0
        for key in counter:
            v = counter[key]
            after += v
            answer.append(after)
            for id in range(before + 1, after):
                answer.append(id)
            before = after
        print(*answer)
    else:
        print(-1)
