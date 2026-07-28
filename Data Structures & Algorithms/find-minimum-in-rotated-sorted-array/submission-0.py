class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        n = len(nums) // 2
        while l < r:
            if nums[l] > nums[n]:
                r = n
                l += 1
                n = (l + r) // 2
            elif nums[n] > nums[r]:
                l = n + 1
                n = (l + r) // 2
            elif nums[l] < nums[r]:
                return nums[l]
        return nums[n]