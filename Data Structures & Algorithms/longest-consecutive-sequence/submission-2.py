class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        maxLen = 0
        for num in numbers:
            if num - 1 not in numbers:
                count = 1
                current = num
                while current + 1 in numbers:
                    count += 1
                    current += 1
                maxLen = max(count,maxLen)
        return maxLen