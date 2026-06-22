class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = []
        for i in range(1,100):
            if i not in nums:
                return i