import sys
sys.setrecursionlimit(2000)

if __name__=="__main__":
    T = int(input())
    def DFS(i):
        if visited[inp[i]] == 0: # 방문하지 않았다면?
            visited[inp[i]] = 1 # 방문해써욤
            DFS(inp[i])

    while T > 0:
        count = 0
        N = int(input())
        # 1 부터 N 까지의 정수 N개.
        inp = []
        inp = list(map(int, list(input().split())))
        inp = [0] + inp

        visited = [0]*(N+1)

        # DFS 로 풀어야지 DFS 되면 count

        for i in range(1, N+1):
            if visited[i] == 0 : #방문하지 않았다면
                visited[i] = 1
                DFS(i)
                count += 1

        T-=1
        print(count)