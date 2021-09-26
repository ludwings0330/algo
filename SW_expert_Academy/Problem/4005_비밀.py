# 각 아이들이 친하다고 생각하는 친구들의 수를 구하자
# 또한 어떤 비밀이 전달될 수 있는 가장 긴 길이도 구하자


T = int(input())


def dfs(current, cnt):
    ret = cnt
    if current in graph:
        for next in graph[current]:
            if not visit[next]:
                visit[next] = True
                ret = max( ret, dfs(next, cnt + 1))
                visit[next] = False
    return ret

for testCase in range(1, T+1):
    N, K = map(int, input().split())
    # 아이들의 수 N, 말한 비밀의 수 K
    secrets = []

    parent = [i for i in range(N+1)]
    rank = [1 for i in range(N+1)]

    for i in range(K):
        secrets.append(list(map(int, input().split())))

    graph = {}

    for secret in secrets:
        for current in range(1, len(secret) - 1):
            if secret[current] in graph:
                graph[secret[current]][secret[current+1]] = 1
            else:
                graph[secret[current]] = {secret[current+1] : 1}

    MAX = 0
    for i in range(1, N+1):
        visit = [False] * (N+1)
        visit[i] = True
        MAX = max(MAX, dfs(i, 1))
        visit[i] = False
    print("#%d" %testCase, end=' ')
    for i in range(1, N+1):
        if i in graph:
            print(len(graph[i]), end =' ')
        else:
            print(0, end=' ')

    print(MAX)
    # 비밀이 전달될 수 있는 가장 긴 길이?
