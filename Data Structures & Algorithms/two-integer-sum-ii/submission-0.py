class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Since the array is sorted in ascending
        # we use two pointer approach to save space
        left, right = 0, len(numbers)-1

        while left < right:
            cur_sum = numbers[left] + numbers[right]
            if cur_sum == target:
                return [left+1, right+1]
            if cur_sum < target:
                left += 1
            if cur_sum > target:
                right -= 1
        
