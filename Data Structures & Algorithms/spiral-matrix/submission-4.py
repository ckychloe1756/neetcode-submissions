class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        horizontal_steps = len(matrix[0])
        vertical_steps = len(matrix) - 1
        r, c, d = 0, -1, 0
        while True:
            if d == 0 or d == 2:
                num_steps = horizontal_steps
            else:
                num_steps = vertical_steps
            if num_steps == 0:
                break
            for _ in range(num_steps):
                r += directions[d][0]
                c += directions[d][1]
                res.append(matrix[r][c])
            if d == 0 or d == 2:
                horizontal_steps -= 1
            else:
                vertical_steps -= 1
            d = (d + 1) % 4
        return res