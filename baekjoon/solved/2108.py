import sys
import math
input = sys.stdin.readline

N = int(input())
nums = []
MAX = 1
dic = {}
SUM = 0
for i in range(N):
    a = int(input())
    if a in dic:
        dic[a] += 1
        MAX = max(MAX , dic[a])
    else:
        dic[a] = 1
    nums.append(a)
    SUM += a

ans1 = round(SUM/N)
nums.sort()
ans2 = nums[N//2]

c = 0
setNums = sorted(set(nums))
ans3  = nums[0]
for i, n in enumerate(setNums):
    if dic[n] == MAX:
        c += 1
        ans3 = n
        if c == 2:
            break
ans4 = nums[-1] - nums[0]
print(ans1, ans2, ans3, ans4,sep ='\n')