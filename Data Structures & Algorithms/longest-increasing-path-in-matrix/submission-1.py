class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        dp = {}
        def dfs(r, c, prev_val):
            if not 0 <= r < rows or not 0 <= c < cols or matrix[r][c] <= prev_val:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            res = 1
            for dr, dc in directions:
                res = max(res, 1 + dfs(r + dr, c + dc, matrix[r][c]))
            dp[(r, c)] = res
            return res
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, float('-inf'))
        return max(dp.values())