import sys
inp = sys.stdin.readline

N, M = map(int, inp().rstrip().split())
print(N, M)
hDict = {}
sumDict = {i:0 for i in range(1,N+1)}
visit = [False] * (N+1)

def addNode(key, value): # key -> value
    sumDict[value] += sumDict[key] + 1 # 내보다 작은건 하나 추가 된거야.
    if value in hDict:
        for node in hDict[value]:
            sumDict[key] += sumDict[value] + 1
    else:
        sumDict[key] += sumDict[value] + 1


for i in range(M):
    key, value = map(int, inp().rstrip().split())
    if key in hDict:
        hDict[key].append(value)
    else:
        hDict[key] = [value]

    addNode(key, value)

print(hDict)
print(sumDict)
