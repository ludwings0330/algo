# 부분수열의 합
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
visit = [False] * 2000001

def recursiveSolve(i, SUM):
    visit[SUM] = True
    if i == N:
        return
    recursiveSolve(i+1, SUM)
    recursiveSolve(i+1, SUM + arr[i])

recursiveSolve(0, 0)

for i in range(1, 2000001):
    if not visit[i]:
        print(i)
        break