num = 1
for _ in range(3):
    num *= int(input())
nums = [0]*10

while num:
    nums[num%10]+=1
    num//=10
for i in nums:
    print(i)