import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()

t = int(input())

for test_case in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    counter = Counter(a)


    candidates = []
    for key, value in counter.items():
        if value >= k:
            candidates.append(key)

    candidates.sort()

    answer = -1
    if not candidates:
        print(-1)
    else:
        l, r = 0, 1
        answer = 1
        answer_l, answer_r = 0, 0

        while r < len(candidates):
            if candidates[r] - candidates[r-1] != 1:
                l, r = r, r+1
                continue
            if answer < r - l + 1:
                answer_l = l
                answer_r = r
                answer = r - l + 1
            r += 1

        print(candidates[answer_l], candidates[answer_r])
