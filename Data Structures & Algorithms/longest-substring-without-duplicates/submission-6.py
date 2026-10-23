class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_map = {}
        left = 0
        max_len = 0

        for r in range(len(s)):
            if s[r] in str_map:
                left = max(str_map[s[r]] + 1, left)
            str_map[s[r]] = r
            max_len = max(max_len, r - left + 1)
        return max_len