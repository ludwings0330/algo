# 3초 1 GB
import sys
input = sys.stdin.readline

N, K, L = map(int, input().split())
teamList = []
count = 0

for _ in range(N):
    a, b, c = map(int, input().split())
    if a+b+c >= K and a>=L and b>=L and c>=L:
        count += 1
        teamList.append([a, b, c])

print(count)
for team in teamList:
    print(*team, end = ' ')