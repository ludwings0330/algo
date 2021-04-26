tileList = [0, 1, 1]

N = int(input())
answer = 0

for i in range(2, N+1):
    tileList.append(tileList[i] + tileList[i-1])

answer = (tileList[-1] + tileList[-2]) * 2
print(answer)