import sys
input = lambda:sys.stdin.readline().rstrip()


'''
건물 N개
구름다리 M개

색은 1 이상의 정수로 표시
각 건물은 한가지 색으로
연결된 건물은 다른 색으로
1번부터 N번까지 색을 차례대로 나열했을 때 사전순으로 가장 앞서도록,
    -> 앞에 있는 건물은 최대한 작은 정수로 칠하기 
'''

N, M = map(int, input().split())
graph = {}
for _ in range(M):
    s, e = map(int, input().split())
    if s in graph:
        graph[s][e] = 1
    else:
        graph[s] = {e:1}

    if e in graph:
        graph[e][s] = 1
    else:
        graph[e] = {s:1}

color = [-1] * (N+1)
color[1] = 1

for current in range(2, N+1):
    color[current] = 1
    if current in graph:
        arr = [[color[next], next] for next in graph[current]]
        arr.sort(key = lambda x : x[0])
        for c, n in arr:
            if color[current] == c:
                color[current] += 1
print(*color[1:])