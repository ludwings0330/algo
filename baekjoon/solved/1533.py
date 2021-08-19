# Title : 길의 개수
# Tag : 인접 행렬, 분할 정복 거듭 제곱
import sys
input = lambda: sys.stdin.readline().rstrip()

N, S, E, T = map(int, input().split())

S, E = S-1, E-1
MATRIX = [[0] * (N*5) for _ in range(N*5)]

for i in range(N):
    line = list(map(int, list(input())))
    for j in range(N):
        t = line[j]
        if t == 1:
            MATRIX[i*5][j*5] = 1
        if t >= 2:
            MATRIX[i*5][j*5 + (t - 1)] = 1

for i in range(N):
    for dt in range(1, 5):
        MATRIX[i*5 + dt][i*5 + dt - 1] = 1

def mul_mat(A, B):
    M = len(A)
    ret = [[0] * M for _ in range(M)]

    for i in range(M):
        for j in range(M):
            for k in range(M):
                ret[i][j] += A[i][k] * B[k][j]
                ret[i][j] %= 10**6+3

    return ret

def pow(A, n):
    if n == 1:
        return A
    if n % 2 == 1:
        return mul_mat(A, pow(A, n-1))
    if n %2 == 0:
        mat = pow(A, n//2)
        return mul_mat(mat, mat)

ans = pow(MATRIX, T)
print(ans[S*5][E*5])