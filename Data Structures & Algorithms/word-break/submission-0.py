class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        s_len = len(s)
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                w_len = len(w)
                if i + w_len <= s_len and s[i : i + w_len] == w:
                    dp[i] = dp[i + w_len]
                if dp[i]:
                    break
        return dp[0]

