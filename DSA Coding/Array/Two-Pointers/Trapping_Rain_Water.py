#https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) < 3:
            return 0
        trappedWater = 0
        maxLeft = height[0]
        maxRight = height[-1]
        left = 1
        right = len(height) - 2
        while left <= right:
            if maxLeft <= maxRight:
                if height[left] >= maxLeft:
                    maxLeft = height[left]
                else:
                    trappedWater += maxLeft - height[left]
                left += 1
            else:
                if height[right] >= maxRight:
                    maxRight = height[right]
                else:
                    trappedWater += maxRight - height[right]
                right -= 1
        return trappedWater