class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            cur = root
            for char in w:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
            cur.word = w  # Attach full word at leaf node

        ROWS, COLS = len(board), len(board[0])
        res = []

        def backtrack(r, c, parent_node):
            char = board[r][c]
            curr_node = parent_node.children[char]

            # 1. Match Found! Append word and clear to prevent duplicate entries
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None

            # 2. Mark current cell visited
            board[r][c] = '#'

            # 3. Explore 4-directional neighbors
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                # Check grid bounds & ensure neighbor char exists in Trie branch
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != '#': 
                    if board[nr][nc] in curr_node.children:
                        backtrack(nr, nc, curr_node)
            # 4. Unmark visited (backtrack state)
            board[r][c] = char

            # 5. Trie Pruning: Remove empty leaf nodes to speed up search
            if not curr_node.children:
                parent_node.children.pop(char)

        # -------------------------------------------------------------
        # STEP 3: Kick off DFS from every board cell matching Trie root
        # -------------------------------------------------------------
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    backtrack(r, c, root)

        return res