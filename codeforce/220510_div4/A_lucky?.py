n = int(input())

nums = []
for i in range(n):
    nums.append(list(map(int, input())))

for num in nums:
    if sum(num[:3]) == sum(num[3:]):
        print("YES")
    else:
        print("NO")