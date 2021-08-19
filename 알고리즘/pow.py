def pow(A, n):
    if n == 1:
        return A
    if n%2 == 0:
        mat = pow(A, n//2)
        return mul_mat(mat, mat)
    if n%2 == 1:
        return mul_mat(A, pow(A, n-1))

def mul_mat(A, B):
    M = len(A)
    ret = [[0] * M for _ in range(M)]

    for i in range(M):
        for j in range(M):
            for k in range(M):
                ret[i][j] += A[i][k] * B[k][j]

    return ret