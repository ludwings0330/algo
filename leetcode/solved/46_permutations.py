class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        from itertools import permutations

        return permutations(nums, len(nums))

print(Solution().permute([1, 2, 3]))