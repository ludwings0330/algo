TC = int(input())


def solve(toPick):
    if toPick == 0:
        global ans
        ans = min(ans, get_dist())
        return

    for i in range(N):
        if not visit[i]:
            path.append(i)
            visit[i] = True

            solve(toPick - 1)

            visit[i] = False
            path.pop()
    return

def get_dist():
    current_x, current_y = company
    ret = 0

    for next in path:
        next_x = customer[next*2]
        next_y = customer[next*2 +1]
        ret += abs(current_x - next_x) + abs(current_y - next_y)
        current_x = next_x
        current_y = next_y

    ret += abs(current_x - home[0]) + abs(current_y - home[1])

    return ret

for i in range(1, TC + 1):
    print("#{}".format(i), end = ' ')
    N = int(input())
    pos = list(map(int, input().split()))

    company = pos[:2]
    home = pos[2:4]
    customer = pos[4:]

    path = []
    visit = [False] * N
    ans = 10**9

    solve(N)
    print(ans, end =' ')
    print()