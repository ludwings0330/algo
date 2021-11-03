import sys
sys.setrecursionlimit(10**9)
input = lambda: sys.stdin.readline().rstrip()
MOD = 10**6
A = [[0, 1], [1, 1]]
def sq(A, B):
    retMat = [[0, 0], [0, 0]]
    retMat[0][0] = (A[0][0]*B[0][0] + A[0][1]*B[1][0])%MOD
    retMat[0][1] = (A[0][0]*B[0][1] + A[0][1]*B[1][1])%MOD
    retMat[1][0] = (A[1][0]*B[0][0] + A[1][1]*B[1][0])%MOD
    retMat[1][1] = (A[1][0]*B[0][1] + A[1][1]*B[1][1])%MOD

    return retMat

def solve(n):
    if n == 1:
        return A
    if n % 2 == 0:
        B = solve(n//2)
        return sq(B, B)
    else:
        return sq(A, solve(n-1))
N = int(input())

print(solve(N)[1][0])