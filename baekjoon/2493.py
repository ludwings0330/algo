import sys
input = sys.stdin.readline

N = int(input())
towerDict = dict()
towerList = list(map(int, input().split()))
for i, height in enumerate(towerList):
    if height in towerDict:
        towerDict[height].append(i+1)
    else:
        towerDict[height] = [i+1]
towerDict.sort()

for towers in towerDict:
    for towerIndex 