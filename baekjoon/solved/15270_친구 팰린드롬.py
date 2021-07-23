if __name__ == "__main__":
    N, M = map(int, input().split())
    areFriends = [[0]*(N+1) for i in range(N+1)]
    visit = [False] * (N+1)

    for i in range(M):
        a, b = map(int, input().split())
        areFriends[a][b] = 1
        areFriends[b][a] = 1

    def recursiveSolve(ivisit):
        finished = True

        for i in range(1, N+1):
            if not finished:
                break
            if not ivisit[i]:
                for j in range(i+1, N+1):
                    if not ivisit[j] and areFriends[i][j] == 1:
                        finished = False
                        num = i
                        break

        if finished:
            return 0

        ret = 0

        for i in range(num+1, N+1):
            if not visit[i] and not visit[num] and areFriends[i][num] == 1: # 둘다 방문 안했고 둘이 친구라면
                ivisit[i] = ivisit[num] = True # 방문표시
                ret = max(ret, 2 + recursiveSolve(ivisit))
                ivisit[i] = ivisit[num] = False # 다시 돌아와!

        return ret

    answer = recursiveSolve(visit)

    if N-answer > 0:
        answer += 1

    print(answer)