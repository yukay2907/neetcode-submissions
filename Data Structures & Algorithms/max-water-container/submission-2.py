class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        i = 0
        j = len(heights)-1
        
        while i < j:
            height = min(heights[i],heights[j])
            width = j-i
            water = height * width
            maxWater = max(maxWater,water)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return maxWater