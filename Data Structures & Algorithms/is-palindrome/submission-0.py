class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_s = ''
        for letter in s:
            if ord('A') <= ord(letter) <= ord('Z') or ord('a') <= ord(letter) <= ord('z') or ord('0') <= ord(letter) <= ord('9'):
                valid_s += letter.lower()
        i = 0
        while i <= len(valid_s) // 2 - 1:
            if valid_s[i] != valid_s[-i-1]:
                return False
            i += 1
        
        return True