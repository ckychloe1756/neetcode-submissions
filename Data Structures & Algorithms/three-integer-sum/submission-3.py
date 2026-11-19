class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i, num1 in enumerate(nums):
            if num1 > 0:
                break
            if i > 0 and num1 == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = num1 + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    triplets.append([num1, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return triplets
            