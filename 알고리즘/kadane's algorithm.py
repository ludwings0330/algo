a = list(map(int, input().split()))

dp = [a[0]]
for i in range(1, len(a)):
    dp.append(max(dp[-1] + a[i], a[i]))
print(max(dp))
