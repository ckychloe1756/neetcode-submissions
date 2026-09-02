class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        prev = list(range(n + 1))
        cur = [0] * (n + 1)

        for i in range(1, m + 1):
            cur[0] = i
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    cur[j] = prev[j-1]
                else:
                    cur[j] = min(prev[j-1] + 1, prev[j] + 1, cur[j-1] + 1)
                
            prev = cur
            cur = [0] * (n + 1)
        return prev[-1]