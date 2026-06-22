class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(i,curr_set):
            if i == len(nums):
                result.append(curr_set.copy())
                return
            
            curr_set.append(nums[i])
            dfs(i+1,curr_set)

            curr_set.pop()

            dfs(i+1,curr_set)
        
        dfs(0,[])
        return result