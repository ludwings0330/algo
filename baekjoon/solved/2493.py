import sys
input = sys.stdin.readline

N = int(input())
towerList = [0] + list(map(int, input().split()))

MAX = 0
ret = []
stack = []
for i in range(1, N+1):
    if MAX < towerList[i]:
        ret.append(0)
        MAX = towerList[i]
        stack.append([towerList[i], i])
    else:
        while len(stack) > 0 and stack[-1][0] < towerList[i]:
            stack.pop()
        ret.append(stack[-1][1])
        stack.append([towerList[i], i])

print(*ret)