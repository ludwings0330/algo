import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
heights = list(map(int, input().split()))
ans = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        flag = True

        if i == j:
            continue
        inclination = (heights[j] - heights[i]) / (j-i)

        for k in range(min(i, j)+1, max(i, j)):
            k_inclination = (heights[k] - heights[i]) / (k - i)

            if k_inclination >= inclination:
                flag = False
                break
        if flag:
            cnt += 1
    ans = max(ans, cnt)
print(ans)