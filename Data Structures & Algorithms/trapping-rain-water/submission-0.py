class Solution:
    def trap(self, height: List[int]) -> int:
        # Watch neetcode video - first learn the extra space solution
        # then the two-pointer solution
        if not height: return 0

        l, r = 0, len(height)-1
        maxLeft, maxRight = height[l], height[r]
        res = 0

        while l < r:
            if maxLeft < maxRight:  # we move the left pointer
                l += 1
                maxLeft = max(maxLeft, height[l])
                res += (maxLeft - height[l])
            else:   # we move the right pointer
                r -= 1
                maxRight = max(maxRight, height[r])
                res += (maxRight - height[r])
        return res
