class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_area = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(r, c):
            area = 0
            if grid[r][c]:
                area += 1
                grid[r][c] = 0
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        area += dfs(nr, nc)
            return area

        for r in range(m):
            for c in range(n):
                area = dfs(r, c)
                max_area = max(max_area, area)
        return max_area