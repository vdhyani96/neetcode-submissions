class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # let's try using two-pointer
        max_water = 0

        left, right = 0, len(heights)-1
        while left < right:
            water_level = min(heights[left], heights[right])
            water_area = water_level * (right-left)
            max_water = max(max_water, water_area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return max_water