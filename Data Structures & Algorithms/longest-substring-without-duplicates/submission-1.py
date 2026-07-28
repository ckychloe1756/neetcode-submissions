class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        str_dict = {}
        l = 0
        for i in range(len(s)):
            if s[i] in str_dict:
                l = max(l, str_dict[s[i]] + 1)
            str_dict[s[i]] = i
            length = max(length, i - l + 1)
        return length