class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    dfs(nr, nc)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    num += 1
        return num
