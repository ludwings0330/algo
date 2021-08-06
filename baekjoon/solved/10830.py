import sys
input = sys.stdin.readline

N, B = map(int, input().split())
# 1<=B<=100000000000000
# 2 <= N <= 5
A = []
for y in range(N):
    A.append(list(map(int, input().split())))
# A의 B 승 출력하기
# 분할로 합시다~
n = 1
I = [[0]*N for _ in range(N)]
for y in range(N):
    for x in range(N):
        if x == y:
            I[y][x] = 1
def mul(A, B):
    ret = [[0]*N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            SUM = 0
            for i in range(N):
                SUM += A[y][i] * B[i][x]
            ret[y][x] = SUM % 1000
    return ret

def solve(n):
    if n == 1:
        return mul(A, I)
    if n == 2:
        return mul(A, A)
    ret = A
    if n%2 == 1:
        a = (solve(n//2))
        b = mul(a, A)
        ret = mul(a, b)
    else:
        a = (solve(n//2))
        ret = mul(a, a)
    return ret

ans = solve(B)

for l in ans:
    print(*l,sep=' ')