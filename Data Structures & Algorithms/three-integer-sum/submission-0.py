class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for i in range(len(nums)):
            target = -nums[i]
            for j in range(i + 1, len(nums)):
                k = target - nums[j]
                if k in nums[j + 1:]:
                    triplet = sorted([nums[i], nums[j], k])
                    if triplet not in answer:
                        answer.append(triplet)
        return answer