import sys
input = sys.stdin.readline


nums = [0]
root_index = 1
while True:
    n = input()
    if n == '':
        break

    nums.append(int(n))
tree =[0] * (len(nums) + 1)
tree[1], tree[2] = nums[1], nums[2]

for i in range(3, len(nums)):
    if nums[root_index] > 