class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         arr_set = set(nums)
         return len(arr_set) != len(nums)