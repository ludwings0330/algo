import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())


#
def solve(remains):
    if remains == 0:
        return

    s1, s2 = -1, -1
    for i in range(n):
        if s1 == -1 and not visit[i]:
            s1 = i
        elif s1 != -1 and not visit[i]:
            s2 = i
            break

    buries = (a[s1] + a[s2]) // k


while t:
    t -= 1
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    visit = [False] * n
    cache = [-1] * n
