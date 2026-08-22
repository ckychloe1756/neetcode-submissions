class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            i = ord(w) - ord('a')
            if cur.children[i] == None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            i = ord(w) - ord('a')
            cur = cur.children[i]
            if not cur:
                return False
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            i = ord(w) - ord('a')
            cur = cur.children[i]
            if not cur:
                return False
        return True
        