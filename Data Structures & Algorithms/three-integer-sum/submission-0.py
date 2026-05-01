class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        for i in range(len(nums)):
            diff1 = 0 - nums[i]
            hashset = set()
            for j in range(i+1, len(nums)):
                diff2 = diff1 - nums[j]
                if diff2 in hashset:
                    res.add(tuple(sorted((nums[i], nums[j], diff2))))
                hashset.add(nums[j])
        return [list(item) for item in res]