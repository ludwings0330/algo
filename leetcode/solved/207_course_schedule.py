from collections import defaultdict

class Solution:
    def canFinish(self, numCourse: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            # a 를 하려면 b 가 선행되어야함
            graph[a].append(b)

        traced = set()
        visited = set()

        def dfs(current):
            if current in traced:
                return False

            if current in visited:
                return True

            traced.add(current)
            for pre in graph[current]:
                if not dfs(pre):
                    return False

            traced.remove(current)
            visited.add(current)
            return True

        result = True
        for i in range(numCourse):
            if not dfs(i):
                return False

        return True


numCourse = 2
prerequisties = [[1, 0], [0, 1]]
print(Solution().canFinish(numCourse, prerequisties))

prerequisties = [[1, 0]] # 1을 하려면 0 부터 해
print(Solution().canFinish(numCourse, prerequisties))
