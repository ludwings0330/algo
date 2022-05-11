import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

for test_case in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    import collections
    counter = collections.Counter(a)


    candidates = []
    for key, value in counter.items():
        if value >= k:
            candidates.append(key)

    candidates.sort()

    answer = -1
    if not candidates:
        print(-1)
    else:
        l = r = candidates[0]
        gap = 0

        tmp_l = l
        tmp_r = r
        for i in range(1, len(candidates)):
            if tmp_r + 1 == candidates[i]:
                tmp_r += 1
                if gap < tmp_r - tmp_l:
                    gap = tmp_r - tmp_l
                    l = tmp_l
                    r = tmp_r
            else:
                tmp_l = tmp_r = candidates[i]

        print(l, r)
