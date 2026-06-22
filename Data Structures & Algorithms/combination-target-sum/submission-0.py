class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset=[]
        def dfs(i):
            cur_sum = sum(subset)
            if cur_sum > target:
                return
            if cur_sum == target:
                result.append(subset.copy())
                return
            if i >= len(nums):
                return
            
            subset.append(nums[i])
            dfs(i)

            subset.pop()

            dfs(i+1)
        dfs(0)
        return result