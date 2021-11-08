import sys
input = lambda: sys.stdin.readline().rstrip()

A, B, C = map(int, input().split())
N = int(input())
ans = 0

while N:
    N -= 1
    tmp = 0
    for i in range(3):
        a, b, c = map(int, input().split())
        tmp += (a*A) + (b*B) + (c*C)
    ans = max(ans, tmp)
print(ans)