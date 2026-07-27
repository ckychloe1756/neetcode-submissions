class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            a[sorted_s].append(s)
        return a.values()