# Title : 본대 산책2
# Tag ; 분할 정복을 이용한 거듭 제곱, 인접행렬의 거듭제곱

import sys
input = lambda: sys.stdin.readline().rstrip()

M = [[0, 1, 1, 0, 0, 0, 0, 0],
     [1, 0, 1, 1, 0, 0, 0, 0],
     [1, 1, 0, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 1, 0, 0],
     [0, 0, 1, 1, 0, 1, 0, 1],
     [0, 0, 0, 1, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 1, 0, 1],
     [0, 0, 0, 0, 1, 0, 1, 0]]

def exp(n):
    if n == 1:
        return M

    if n % 2 == 1:
        A = exp(n-1)
        return mul(A, M)

    elif n % 2 == 0:
        A = exp(n//2)
        return mul(A, A)


def mul(A, B):
    ret = [[0] * 8 for _ in range(8)]

    for i in range(8):
        for j in range(8):
            for k in range(8):
                ret[i][j] += A[i][k] * B[k][j]
                ret[i][j] %= 1000000007
    return ret

d = int(input())
print(exp(d)[0][0])