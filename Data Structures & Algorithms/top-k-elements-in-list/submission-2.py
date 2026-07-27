class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_set = set(nums)
        num_dict = defaultdict(list)
        for n in num_set:
            num_dict[nums.count(n)].append(n)
        freq_list = sorted(num_dict.keys(), reverse = True)
        ans = []
        i = 0
        while len(ans) < k:
            ans += num_dict[freq_list[i]]
            i += 1
        return ans