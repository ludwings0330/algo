# import sys
# input = lambda: sys.stdin.readline().rstrip()
# from collections import defaultdict
# from collections import deque
#
# t = int(input())
#
# while t:
#     t -= 1
#
#     n = int(input())
#     parents = [0, 0] + list(map(int, input().split()))
#     colors = ['B'] + list(input())
#     remains = defaultdict(int)
#     graph = {}
#     for i, parent in enumerate(parents):
#         if i == 0:
#             continue
#         remains[parent] += 1
#
#     dq = deque()
#     for node in range(n + 1):
#         if colors[node] == 'W':
#             graph[node] = [1, 0]
#         else: # 'B'
#             graph[node] = [0, 1]
#
#         if remains[node] == 0:
#             dq.append(node)
#
#     while dq:
#         current = dq.popleft()
#         parent = parents[current]
#         graph[parent] = [c + p for c, p in zip(graph[current], graph[parent])]
#
#         remains[parent] -= 1
#         if remains[parent] == 0:
#             dq.append(parent)
#
#     count = 0
#     for i in range(1, n+1):
#         if graph[i][0] == graph[i][1]:
#             count += 1
#     print(count)
#

# solution
import sys
from collections import defaultdict
sys.setrecursionlimit(10**5)
input = lambda: sys.stdin.readline().rstrip()
t = int(input())

while t:
    t -= 1
    n = int(input())

    childs = defaultdict(list)
    colors = defaultdict(str)

    for i, parent in enumerate(list(map(int, input().split()))):
        childs[parent].append(i+2)

    for i, color in enumerate(list(input())):
        colors[i+1] = color

    global result
    result = 0

    def dp(current):
        bal = 1 if colors[current] == 'W' else -1

        if len(childs[current]) == 0:
            return bal

        for child in childs[current]:
            bal += dp(child)

        if bal == 0:
            global result
            result += 1
        return bal

    dp(1)
    print(result)
