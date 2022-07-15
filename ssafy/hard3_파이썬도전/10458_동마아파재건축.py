idx = int(input())
arr = list(map(int, input().split()))[:idx+1]
max_height = -1
ans = 0
for num in arr[::-1]:
    if max_height == -1:
        max_height = num
        ans += 1
    elif max_height <= num:
        max_height = num
        ans += 1
print(ans)
