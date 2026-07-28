class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Using sliding window with dictionary
        length = 0
        str_dict = {}
        l = 0
        for i in range(len(s)):
            if s[i] in str_dict:
                l = max(l, str_dict[s[i]] + 1) # max() so that l is the next index of last charater which got repeated
            str_dict[s[i]] = i
            length = max(length, i - l + 1)
        return length

        # # Using sliding window with set()
        # charSet = set()
        # l = 0
        # res = 0

        # for r in range(len(s)):
        #     while s[r] in charSet:
        #         charSet.remove(s[l])
        #         l += 1
        #     charSet.add(s[r])
        #     res = max(res, r - l + 1)
        # return res