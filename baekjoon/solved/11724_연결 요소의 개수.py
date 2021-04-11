import sys

if __name__ == "__main__":
    N, M = map(int, input().split())
    dicLine = {i:[i] for i in range(1,N+1)}
    visit =[0]*(N + 1)

    for i in range(M):
        f, t = map(int, sys.stdin.readline().rstrip().split())

        dicLine[f].append(t)
        dicLine[t].append(f)

    def DFS(num):
        if visit[num] == 1:
            # already visit
            return 0
        stack = []
        stack.append(num)
        visit[num] = 1

        while stack:
            node = stack.pop()
            toList = dicLine[node]
            for i in toList:
                if visit[i] == 0:
                    # didnt visit
                    stack.append(i)
                    visit[i] = 1
        return 1
    count = 0
    for num in dicLine:
        count += DFS(num)
    print(count)