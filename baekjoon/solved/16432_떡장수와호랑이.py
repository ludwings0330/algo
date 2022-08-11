import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**5 + 1)

N = int(input())
days = [list(map(int, input().split())) for _ in range(N)]
path = []
cache = [[False] * 10 for _ in range(N)]

def dfs(day, cake):
    if day == N:
        return True

    # 이미 방문했으면 더 진입 안함
    if cache[day][cake]:
        return False

    cache[day][cake] = True
    for eat_cake in days[day][1:]:
        if cake == eat_cake:
            continue
        if dfs(day+1, eat_cake):
            path.append(eat_cake)
            return True

    return False


dfs(0, -1)
if len(path) > 0:
    print(*path[::-1], sep='\n')
else:
    print(-1)
