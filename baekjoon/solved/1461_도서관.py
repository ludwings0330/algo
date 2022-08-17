import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
right = []
left = []
pos = list(map(int, input().split()))
for i in pos:
    if i > 0:
        right.append(i)
    else:
        left.append(i)
right.sort()
left.sort()

ans = 0
dist = 0

for i in range(0, len(left), M):
    ans += dist
    dist = abs(left[i])
    ans += dist

for i in range(0, len(right), M):
    ans += dist
    dist = right[i]
    ans += dist

print(ans)
