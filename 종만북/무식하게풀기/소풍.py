def recursive_pick(visit: list[bool]):
    idx = -1
    for i in range(n):
        if not visit[i]:
            idx = i
            break

    if idx == -1:
        return 1

    ret = 0
    for f in range(idx+1, n):
        if not visit[f] and is_friend[idx][f]:
            visit[idx] = visit[f] = True
            ret += recursive_pick(visit)
            visit[idx] = visit[f] = False

    return ret


tc = int(input())
while tc:
    tc -= 1
    n, m = map(int, input().split())

    is_friend = [[False] * n for _ in range(n)]
    input_friend = list(map(int, input().split()))
    for i in range(0, len(input_friend), 2):
        a = input_friend[i]
        b = input_friend[i + 1]
        is_friend[a][b] = is_friend[b][a] = True

    visit = [False] * n
    print(recursive_pick(visit))
