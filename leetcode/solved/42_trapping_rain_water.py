class Solution:
    def trap(self, height: list[int]) -> int:
        volume = 0
        stack = []

        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()

                if not stack:
                    break

                distance = i - stack[-1] - 1
                water = min(height[i], height[stack[-1]]) - height[top]
                volume += water * distance
            stack.append(i)
        return volume
# 1 <= n <= 2 * 10**4
# 0 <= height[i] <= 10**5
height = [3, 0, 1, 0, 2]
print(Solution().trap(height))
