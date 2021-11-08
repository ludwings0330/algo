import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
mass = list(map(int, input().split()))
mass.sort()

if mass[0] != 1:
    ans = 1
else:
    SUM = 1

    for i in range(1, N):
        if SUM + 1 < mass[i]:
            break
        SUM += mass[i]

    ans = SUM + 1

print(ans)