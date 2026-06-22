class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def dfs(i,curr_set,remaining):
            if i == len(nums):
                return
            if remaining == 0:
                result.append(curr_set.copy())
            if nums[i] > remaining:
                return

            curr_set.append(nums[i])
            dfs(i,curr_set,remaining-nums[i])
            
            curr_set.pop()
            
            dfs(i+1,curr_set,remaining)

        dfs(0,[],target)
        return result