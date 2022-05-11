class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        answer = 0
        _min = float('inf')

        for price in prices:
            _min = min(_min, price)
            answer = max(max(0, price - _min), answer)
        return answer


prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))
