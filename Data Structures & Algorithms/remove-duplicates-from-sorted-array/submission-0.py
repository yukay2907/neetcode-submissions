class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j = 0,1
        while j<len(nums):
            if nums[i] == nums[j]:
                nums.remove(nums[i])
            else:
                i+=1
                j+=1
        return len(nums)