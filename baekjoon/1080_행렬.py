# 전구 문제와 유사한 그리디 알고리즘
# N, M
import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

A = [list(map(int, list(input()))) for _ in range(N)]
B = [list(map(int, list(input()))) for _ in range(N)]


def transform(r, c):
    for _r in range(r, r + 3):
        for _c in range(c, c + 3):
            A[_r][_c] = (A[_r][_c] + 1) % 2

answer = 0
for r in range(N - 2):
    for c in range(M - 2):
        if A[r][c] != B[r][c]:
            answer += 1
            transform(r, c)

for r in range(N):
    for c in range(M):
        if A[r][c] != B[r][c]:
            answer = -1
            break
    if answer == -1:
        break
print(answer)
