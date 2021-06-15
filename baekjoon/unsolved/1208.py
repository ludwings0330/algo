#부분수열의 합2
# N 개의 정수 다더하면 S 가 되는 경우의 수
# 5 0
# -7 -3 -2 5 8
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
mid = N//2
ldp = {}
rdp = {}
ans = 0
def left(i, SUM):
    if i == mid:
        if SUM in ldp:
            ldp[SUM] += 1
        else:
            ldp[SUM] = 1

        return

    left(i+1, SUM)
    left(i+1, SUM+arr[i])


def right(i, SUM):
    if i == N:
        if SUM in rdp:
            rdp[SUM] += 1
        else:
            rdp[SUM] = 1

        return

    right(i+1, SUM)
    right(i+1, SUM+arr[i])

left(0, 0)
right(mid, 0)

if S == 0:
    ans -= 1
for l in ldp:
    if S-l in rdp:
        ans += ldp[l]*rdp[S-l]
print(ans)