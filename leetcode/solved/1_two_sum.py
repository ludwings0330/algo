class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}

        answer = []

        for i, num in enumerate(nums):
            dict[num] = i

        for i, num in enumerate(nums):
            if target - num in dict and i != dict[target - num]:
                answer = [i, dict[target - num]]
                break

        return answer

nums = [2,7,11,15]
target = 9

print(Solution().twoSum(nums,target))
