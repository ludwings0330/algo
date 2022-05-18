class Solution:
    def to_swap(self, a: int, b: int):
        return str(a) + str(b) < str(b) + str(a)

    def largestNumber(self, nums: list[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j-1], nums[j]):
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
            i += 1

        return ''.join(map(str, nums))
