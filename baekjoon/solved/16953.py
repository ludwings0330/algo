import sys
from collections import deque

input = sys.stdin.readline

A, B = map(int, input().split())

# DFS

dq = deque()
dq.append([A, 1])
ret = sys.maxsize
while dq:
    num, cnt = dq.popleft()
    if num == B:
        ret = min(ret, cnt)

    if num * 2 <= B:
        dq.append([num*2, cnt+1])
    if num*10+1<=B:
        dq.append([num*10+1, cnt+1])
print(ret if ret != sys.maxsize else -1)