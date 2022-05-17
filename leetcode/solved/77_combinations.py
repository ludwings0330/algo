class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        # from itertools import combinations
        # return combinations([i for i in range(1, n+1)], k)
        result = []

        def dfs(i, remains):
            if remains == 0:
                result.append(previous_result.copy())
                return

            for next in range(i+1, n+1):
                previous_result.append(next)
                dfs(next, remains - 1)
                previous_result.pop()

        previous_result = []
        dfs(0, k)
        return result