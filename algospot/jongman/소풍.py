if __name__ == "__main__":
    C = int(input())

    def recursiveSolve(n, visited):
        finished = True
        index = -1
        for i in range(n):
            if not visited[i]:
                # 방문하지 않은 놈이 있다면?
                finished = False
                index = i
                break

        if finished:
            return 1 # 카운트 해준다 ret += recursiveSolve(n, visited)

        ret = 0

        for i in range(i+1, n):
            # 방문하지 않았고 연결되어 있으면 둘다 visited 해주고 재귀 호출
            if not visited[i] and areFriends[index][i] == 1:
                visited[index] = visited[i] = True
                ret += recursiveSolve(n, visited)
                visited[index] = visited[i] = False

        return ret

    while C:
        C -= 1
        N, M = map(int, input().split())
        areFriends = [[0] * N for _ in range(N)]
        visited = [False]*N
        relation = list(map(int, input().split()))

        for i in range(M):
            f, t = relation[i*2], relation[i*2+1]
            areFriends[f][t] = areFriends[t][f] = 1



        print(recursiveSolve(N, visited))