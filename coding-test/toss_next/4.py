# 직접 초대한 사람 수 * 10 + 내가 초대한 사람이 초대한 사람수 * 3 + 내가 초대한 사람이 초대한 사람이 초대한 사람 수 * 1
from collections import defaultdict

def solution(invitationPairs):
    answer = []
    graph = defaultdict(list)

    # s 가 e 를 초대
    for s, e in invitationPairs:
        graph[s].append(e)

    scores = defaultdict(int)
    for current in graph.keys():
        scores[current] += 10 * len(graph[current])
        for next in graph[current]:
            if next in graph:
                scores[current] += 3 * len(graph[next])
                for nextnext in graph[next]:
                    if nextnext in graph:
                        scores[current] += len(graph[nextnext])

    scores = sorted(scores.items(), key=lambda x: x[1], reverse = True)
    return [x[0] for x in scores[:3]]

print(solution([
    [1,2],
    [1,3],
    [3,4],
    [4,5],
    [4,6],
    [4,7]
]))