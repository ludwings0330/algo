class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x:x[0])
        merged = []

        for interval in intervals:
            if merged and interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])

            else:
                merged += interval,
        return merged

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(intervals))