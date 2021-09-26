# Title : 해적과 보석
# Tag : 새로운 기준으로 정렬

import sys
input = lambda: sys.stdin.readline().rstrip()

TC = int(input())
while TC:
    TC -= 1
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    value = [(A[i]+B[i], i) for i in range(N)]
    value.sort(reverse = True)

    score_a = 0
    score_b = 0
    for i in range(N):
        if i % 2 == 0:
            score_a += A[value[i][1]]
        else:
            score_b += B[value[i][1]]
    print(score_a - score_b)