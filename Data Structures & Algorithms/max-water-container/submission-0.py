class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_water = 0

        while l < r:
            length = r - l
            width = min(heights[l],heights[r])
            area = length * width

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

            max_water = max(max_water, area)

        return max_water
    """
    length = r - l
    width = min(height[l],height[r])
    area = length x width
    """

         
        