class Solution:
    def productExceptSelf(self,nums: list[int]) -> list[int]:
        answer = []
        p = 1
        for i in range(len(nums)):
            answer.append(p)
            p *= nums[i]

        p = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= p
            p *= nums[i]
        return answer


nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))
