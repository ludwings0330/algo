if __name__ == "__main__":
    amount = int(input())
    route = int(input())
    stem = [[0]*(amount+1) for i in range(amount+1)]
    visit = [False] * (amount+1)

    # 줄기 초기화.
    for i in range(route):
        pair = list(map(int, input().split()))
        stem[pair[0]][pair[1]] = 1
        stem[pair[1]][pair[0]] = 1
    count = 0

    def BFS():
        # BFS로 풀자!
        # 1번 근처는 전부 감염.
        dq = []
        dq.append(1)
        global count
        visit[1] = True

        while dq:
            node = dq.pop(0)
            for i in range(amount+1):
                if stem[node][i] == 1 and not visit[i]:
                    # 길이 존재하고, 아직 방문하지 않았으면.
                    dq.append(i)
                    visit[i] = True
                    count += 1

    def DFS():
        stack = []
        stack.append(1)
        visit[1] = True
        global count
        while stack:
            node = stack.pop()
            for i in range(amount+1):
                if stem[node][i] == 1 and not visit[i]:
                    # 줄긱 ㅏ있고 방문하지 않았다면
                    stack.append(i)
                    visit[i] = True
                    count += 1

    #BFS()
    DFS()
    print(count)
    pass