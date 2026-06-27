class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        most_water = float('-inf')
        while l < r:
            water = min(heights[l],heights[r]) * (r-l)
            most_water = max(most_water,water)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return most_water