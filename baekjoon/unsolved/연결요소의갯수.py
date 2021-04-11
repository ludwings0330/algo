if __name__ == "__main__":
    N, M = map(int, input().split())
    # N : 정점 갯수
    # M : 간선 갯수
    graph = dict()

    for i in range(M):
        u, v = map(int, input().split())
        if u in graph: # 이미 존재하면
            graph[u].append(v)
        else:
            graph[u] = [v] # 존재하지 않으면 새로 만들어준다.
        if v in graph: # 이미 존재 하면
            graph[v].append(u)
        else:
            graph[v] = [u]
    visit = [False]*(N+1)
    count = 0

    def BFS(start):
        dq = []
        dq.append(graph[start])
        while dq:
            node = dq.pop(0)

            for i in range(len(node)):
                if not visit[node[i]]: #
                    visit[node[i]] = True
                    dq.append(graph[node[i]])
    for i in range(1, N+1):
        if not visit[i]:  # 방문하지 않으면 True
            visit[i] = True
            count+=1
            BFS(i)

    print(count)