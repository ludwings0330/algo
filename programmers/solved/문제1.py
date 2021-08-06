import heapq

def solution(n, costs):
    answer = 0
    VISIT = set()
    hq = []
    graph = {}
    for s, e, v in costs:
        if s in graph:
            graph[s][e] = v
        else:
            graph[s] = {e : v}

        if e in graph:
            graph[e][s] = v
        else:
            graph[e] = {s : v}

    for next in graph[0]:
        heapq.heappush(hq, [graph[0][next], next])
    VISIT.add(0)

    while hq:
        value, node = heapq.heappop(hq)
        if node not in VISIT:
            answer += value
        VISIT.add(node)

        for next in graph[node]:
            if next not in VISIT:
                heapq.heappush(hq, [graph[node][next], next])



    print(graph)
    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

print(solution(n, costs))