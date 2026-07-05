class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        maxi = 0
        for num in nums:
            seen.add(num)
        for num in seen:
            if num-1 not in seen:
                current = num
                count = 1
                while current + 1 in seen:
                    count += 1
                    current += 1
                maxi = max(maxi,count)
        return maxi