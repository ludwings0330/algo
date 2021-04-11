if __name__ =="__main__":
    N = int(input())
    truck = []
    visit = [0]*(N+1) # index 0 ~ N

    for i in range(N):
        truck.append(list(map(int, input().split())))

    # 어느 한 도시에서 출발, 다시 원상태로 돌아와야함.
    def DFS(i):
        stack = []
        stack.append(i)
        visit[i] = 1
        while stack:
            now =