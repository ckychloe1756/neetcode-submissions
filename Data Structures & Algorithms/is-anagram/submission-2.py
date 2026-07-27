class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_s = set(s)
        letter_t = set(t)
        if len(letter_s) != len(letter_t):
            return False
        for l in letter_s:
            if s.count(l) != t.count(l):
                return False
        return True