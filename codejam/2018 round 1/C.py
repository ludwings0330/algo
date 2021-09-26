import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dice = list(map(int, input().split()))

dice.sort()

ans = [[] for _ in range(N)]
cnt = 0
for i in range(N):
    n = dice[i]

    for j in range(N):
        l = len(ans[j])
        if l == 0:
            ans[j].append(n)
            cnt += 1
            break
        elif l <= n:
            ans[j].append(n)
            break

print(cnt)
