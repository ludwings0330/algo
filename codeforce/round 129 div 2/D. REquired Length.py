import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

n, x = map(int, input().split())
ans = -1

dq = deque()
dq.append([x, 0])
visit = set()

while dq:
    current, count = dq.popleft()
    if len(str(current)) == n:
        print(count)
        break
    for k in map(int, set(list(str(current)))):
        if k == 0 or k == 1:
            continue
        if current * k not in visit:
            dq.append([current * k, count + 1])
            visit.add(current*k)
else:
    print(-1)
