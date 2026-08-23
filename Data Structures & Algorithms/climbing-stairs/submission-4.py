class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        dp = [1, 2, 3]
        for i in range(3, n):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]
