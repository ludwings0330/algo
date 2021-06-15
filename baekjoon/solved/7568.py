import sys
input = sys.stdin.readline

N = int(input())
LIST = []
for i in range(N):
    LIST.append(list(map(int, input().split())))
rank = [1]*N
for i in range(N):
    for j in range(N):
        if LIST[i][0] < LIST[j][0] and LIST[i][1] < LIST[j][1]:
            rank[i] += 1
print(*rank)

