class PrefixTree:

    def __init__(self):
        self.trie = {'root': {}}

    def insert(self, word: str) -> None:
        cur = self.trie['root']
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur['end'] = True

    def search(self, word: str) -> bool:
        cur = self.trie['root']
        for w in word:
            if w not in cur:
                return False
            cur = cur[w]
        return cur.get('end', False)

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie['root']
        for w in prefix:
            if w not in cur:
                return False
            cur = cur[w]
        return True
        