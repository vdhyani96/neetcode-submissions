class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                water_level = min(heights[i], heights[j])
                water_area = water_level * (j-i)
                max_water = max(max_water, water_area)
        return max_water