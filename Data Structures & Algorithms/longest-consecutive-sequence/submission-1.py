class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_num = max(nums)
        min_num = min(nums)
        seq = [0] * (max_num - min_num + 1)

        for n in nums:
            seq[n - min_num] += 1
        
        longest = 0
        i = 0
        while i < len(seq):
            comp_len = 0
            while seq[i] != 0:
                comp_len += 1
                i += 1
                if i >= len(seq):
                    break
            if comp_len > longest:
                longest = comp_len
            i += 1
            
        return longest