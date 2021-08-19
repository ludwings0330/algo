# title ; 이사
# tag ; 수학
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

MIN= sys.maxsize
ans = -1

for i in range(N):
    MAX = -1
    for j in range(N):
        dist = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
        if dist > MAX:
            MAX = dist

    if MIN > MAX:
        MIN = MAX
        ans = points[i]
print(*ans)