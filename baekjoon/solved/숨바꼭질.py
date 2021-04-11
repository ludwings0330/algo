import collections

if __name__ == "__main__":
    N, K = map(int, input().split())
    time = 0
    answer = 0
    visit = [0] * 100001
    MAX = 100000
    MIN = 0
    def BFS():
        dq = collections.deque()
        dq.append(N)
        visit[N] = 1 # 방문 했다는 뜻.

        while dq:
            now = dq.popleft()
            if now == K:
                break

            if now * 2 <= MAX:
                if visit[now * 2] == 0:  # 방문하지 않았으면
                    visit[now * 2] = visit[now] + 1
                    dq.append(now*2)
            if now + 1 <= MAX:
                if visit[now + 1] == 0:  # 방문하지 않았으면
                    visit[now + 1] = visit[now] + 1
                    dq.append(now+1)
            if now - 1 >= MIN:
                if visit[now - 1] == 0:  # 방문하지 않았으면
                    visit[now - 1] = visit[now] + 1
                    dq.append(now-1)

    BFS()
    print(visit[K]-1)