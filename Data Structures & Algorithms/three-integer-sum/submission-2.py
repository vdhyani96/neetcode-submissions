class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # using two pointer approach after sorting
        res = set()
        nums.sort()

        for i in range(len(nums)):
            diff1 = 0-nums[i]

            # two-pointer starting now
            left, right = i+1, len(nums)-1
            while left < right:
                cur_sum = nums[left] + nums[right]
                if cur_sum == diff1:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif cur_sum < diff1:
                    left += 1
                elif cur_sum > diff1:
                    right -= 1
        return [list(item) for item in res]


