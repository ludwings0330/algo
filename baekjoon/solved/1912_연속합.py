import sys
input = sys.stdin.readline

n = int(input()) # 1 <= n <= 100,000
numList = [*map(int, input().split())]

answer = numList[0]
dpList = [answer]

for i in range(1, n):
    dpList.append(max(dpList[i-1] + numList[i], numList[i]))
    answer = max(answer, dpList[i])

print(answer)