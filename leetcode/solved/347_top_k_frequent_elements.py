class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        import collections
        counter = collections.Counter(nums)
        answer = []
        counter_list = sorted(list(counter.items()), key = lambda x: -x[1])

        for i in range(k):
            answer.append(counter_list[i][0])
        return answer

print(Solution().topKFrequent([1, 2], 2))
