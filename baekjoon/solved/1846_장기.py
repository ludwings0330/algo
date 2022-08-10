import sys
sys.setrecursionlimit(10**5)

N = int(input())

visit_col = [False] * N
car_pos = [-1] * N


def solve(r):
    if r == N:
        return True
    for c in range(N):
        if visit_col[c]:
            continue
        if r == c or r + c == N-1:
            continue
        visit_col[c] = True
        car_pos[r] = c + 1
        if solve(r+1):
            return True
        car_pos[r] = -1
        visit_col[c] = False
    return False


solve(0)

if car_pos[0] != -1:
    print(*car_pos, sep='\n')
else:
    print(-1)
