class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        row = 0
        col = 0
        min_row = 0
        min_col = 0
        max_row = n - 1
        max_col = m - 1
        spiral = []
        right = True
        down = False
        left = False
        up = False
        while len(spiral) != n*m:
            spiral.append(matrix[row][col])
            if right:
                if col == max_col:
                    right = False
                    down = True
                    min_row += 1
                    row += 1
                else:
                    col += 1
            elif down:
                if row == max_row:
                    down = False
                    left = True
                    max_col -= 1
                    col -= 1
                else:
                    row += 1
            elif left:
                if col == min_col:
                    left = False
                    up = True
                    max_row -= 1
                    row -= 1
                else:
                    col -= 1
            elif up:
                if row == min_row:
                    up = False
                    right = True
                    min_col += 1
                    col += 1
                else:
                    row -= 1
        return spiral
                
                
