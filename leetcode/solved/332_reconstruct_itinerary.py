from collections import defaultdict
from collections import deque
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(deque)

        for ticket in sorted(tickets):
            fr, to = ticket
            graph[fr].append(to)

        route = []

        def dfs(current):
            while graph[current]:
                dfs(graph[current].popleft())
            route.append(current)

        dfs("JFK")
        return route[::-1]

#
# tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# print(Solution().findItinerary(tickets))
#
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# print(Solution().findItinerary(tickets))

tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print(Solution().findItinerary(tickets))
