import collections

if __name__ == "__main__":
    N,M,V = map(int, input().split())

    trunk = [[0] * (N+1) for i in range(N+1)] # 간선있으면 1 없으면 0
    visited = [0] * (N+1) # 방문했으면 1 안했으면 0

    for i in range(M):
        start, end = map(int, input().split())
        trunk[start][end] = 1
        trunk[end][start] = 1


    def DFS(V):
        visited[V] = 1  # 방문한 점 1로 표시
        print(V, end=' ')
        for i in range(1, N + 1):
            if visited[i] == 0 and trunk[V][i] == 1:
                DFS(i)

    DFS(V)
    visited = [0] * (N+1) # 방문했으면 1 안했으면 0
    print()

    def BFS(V):
        dq = collections.deque()
        dq.append(V)
        visited[V] = 1

        while dq:
            n = dq.popleft()
            print(n, end=' ')
            for i in range(1, N+1):
                if visited[i] == 0 and trunk[n][i] == 1: # 방문을 하지 않았고 간선이 존재할때.
                    dq.append(i)
                    visited[i] = 1
    BFS(V)