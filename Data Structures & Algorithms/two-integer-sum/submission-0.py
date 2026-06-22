class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for num,i in enumerate(nums):
            current= target-i
            if current in index_map:
                return [index_map[current],num]
            index_map[i] = num