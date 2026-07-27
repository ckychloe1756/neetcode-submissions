class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        length = len(nums)
        for i in range(length):
            num = nums[i]
            complement = target - num
            if complement in seen:
                return sorted([i, seen[complement]])
            seen[num] = i
