import sys
input = lambda: sys.stdin.readline().rstrip()


T = int(input())
number = 1
while T:
    T -= 1
    answer = 0
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        A, B = B, A
        N, M = M, N

    # N <= M
    for start in range(M-N+1):
        tmp = 0
        for i in range(N):
            tmp += A[i] * B[start + i]

        if tmp > answer:
            answer = tmp

    print(f'#{number} {answer}')
    number += 1
