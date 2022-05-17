class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def dfs(index, path):
            if index == len(nums):
                result.append(path.copy())
                return

            # 추가하거나
            dfs(index+1, path + [nums[index]])
            # 추가하지 않거나
            dfs(index+1, path)

        dfs(0, [])
        return result

print(Solution().subsets([1, 2, 3]))
