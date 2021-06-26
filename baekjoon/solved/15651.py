N, M = map(int, input().split())

def solve(pick, ans):
    if pick == M:
        print(*ans)
        return
    for j in range(1, N+1):
        solve(pick+1, ans + [j])

solve(0, [])