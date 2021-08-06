import sys
input = sys.stdin.readline
import heapq

Q = int(input())
data = {}
ans = 0
while Q:
    Q -= 1
    line = input().rstrip().split()
    i, name, k = int(line[0]), line[1], int(line[2])
    if i == 1:
        c = list(map(int, line[3:]))
    if i == 1: # 정보를 얻음
        if name in data:
            for v in c:
                heapq.heappush(data[name], (-v, v))
        else:
            data[name] = []
            for v in c:
                heapq.heappush(data[name], (-v, v))
    else:
        if name in data:
            while k and data[name]:
                k -= 1
                ans += heapq.heappop(data[name])[1]
print(ans)