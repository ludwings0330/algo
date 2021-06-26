import sys
input = sys.stdin.readline

N = int(input())
points = []
for i in range(N):
    points.append(list(map(int, input().split())))
ret = sorted(points, key = lambda x : (x[1], x[0]))

for p in ret:
    print(*p)