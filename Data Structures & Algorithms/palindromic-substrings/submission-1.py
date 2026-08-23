class Solution:
    def countSubstrings(self, s: str) -> int:
        substrings = 0
        length = len(s)
        for i in range(length):
            # Odd version
            left, right = i, i
            while left >= 0 and right < length and s[left] == s[right]:
                substrings += 1
                left -= 1
                right += 1

            # Even version
            left, right = i, i + 1
            while left >= 0 and right < length and s[left] == s[right]:
                substrings += 1
                left -= 1
                right += 1

        return substrings