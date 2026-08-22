class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        cur = self.trie
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur['end'] = True

    def search(self, word: str) -> bool:
        def dfs(i, cur):
            for j in range(i, len(word)):
                w = word[j]
                if w == '.':
                    for child in cur:
                        if child != 'end' and dfs(j + 1, cur[child]):
                            return True
                    return False
                else:
                    if w not in cur:
                        return False
                    cur = cur[w]
            return cur.get('end', False)

        return dfs(0, self.trie)