class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        ret = 0
        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row = len(grid)
        col = len(grid[0])

        stack = []
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    ret += 1
                    stack = [[r, c]]
                    grid[r][c] = "0"
                    while stack:
                        nr, nc = stack.pop()
                        for dr, dc in move:
                            rr, cc = nr+dr, nc+dc
                            if 0 <= rr < row and 0 <= cc < col and grid[rr][cc] == "1":
                                stack.append([rr, cc])
                                grid[rr][cc] = "0"
        return ret
