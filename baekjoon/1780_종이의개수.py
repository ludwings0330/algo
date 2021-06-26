import sys

def recursiveSolve(N):
    if N == 1:
        return
    nextNum = N//3
    

N = int(input())
paperBoard = []

for i in range(N):
    tmpInputList = list(map(int, sys.stdin.readline().rstrip().split()))
    paperBoard.append(tmpInputList)

print(paperBoard)