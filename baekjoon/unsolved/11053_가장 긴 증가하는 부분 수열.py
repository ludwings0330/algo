
N = int(input())
numList = [0, *map(int, input().split())]
dpList = [0]*(N+1)

for i in range(1, N+1):
    maxIndex = 0

    for j in range(i):
        if numList[i] > numList[j]:
            maxIndex = max(maxIndex, dpList[j])

    dpList[i] = maxIndex + 1

print(max(dpList))