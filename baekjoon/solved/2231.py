N = int(input())
ans = [0]
for i in range(N-1, 0, -1):
    SUM = i
    z = i
    while z:
        SUM += z%10
        z = z//10
    if SUM == N:
        ans.append(i)
print(ans[-1])