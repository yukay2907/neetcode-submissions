class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(ind):
            if ind == len(nums):
                result.append(nums.copy())
                return
            
            for i in range(ind,len(nums)):
                nums[ind], nums[i] = nums[i] ,nums[ind]
                dfs(ind+1)
                nums[ind], nums[i] = nums[i] ,nums[ind]
        dfs(0)
        return result