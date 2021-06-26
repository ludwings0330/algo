#N과 M(4)
N, M = map(int, input().split())

def solve(pick, ans):
    if pick == M:
        print(*ans)
        return
    for j in range(1, N+1):
        if not ans:
            solve(pick+1, [j])
        else:
            if ans[-1] <= j:
                solve(pick+1, ans + [j])

solve(0, [])