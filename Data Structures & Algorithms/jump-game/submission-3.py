class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        jump = 0
        for i in range(n):
            if i <= jump and i + nums[i] >= jump:
                jump = i + nums[i]
        return jump >= (n - 1)