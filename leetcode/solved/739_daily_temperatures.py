class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []

        for day, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                stored_day, tmp = stack.pop()
                answer[stored_day] = day - stored_day
            stack.append([day, temperature])

        return answer



temperatures = [73,74,75,71,69,72,76,73]
print(Solution().dailyTemperatures(temperatures))
