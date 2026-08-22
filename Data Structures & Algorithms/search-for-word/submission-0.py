class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        def search(i, r, c):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= n or c >= m or board[r][c] != word[i] or board[r][c] == '#'):
                return False
            board[r][c] = '#'
            res = (search(i + 1, r - 1, c) or 
                search(i + 1, r + 1, c) or 
                search(i + 1, r, c - 1) or 
                search(i + 1, r, c + 1))
            board[r][c] = word[i]
            return res
        
        for r in range(n):
            for c in range(m):
                if search(0, r, c):
                    return True
        return False
