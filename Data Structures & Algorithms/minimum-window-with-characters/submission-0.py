class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''

        count = defaultdict(int)
        for c in t:
            count[c] += 1

        l = 0
        window = defaultdict(int)
        have = 0
        need = len(count)
        min_window = float('inf')
        answer = ''
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in count and window[s[r]] == count[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < min_window:
                    min_window = r - l + 1
                    answer = s[l:r+1]
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        return answer
