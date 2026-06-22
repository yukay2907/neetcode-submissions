class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        def dfs(i):
            cur_sum = sum(subset)
            if cur_sum > target:
                return
            if cur_sum == target and subset not in result:
                result.append(subset.copy())
            if i >= len(candidates):
                return
            
            subset.append(candidates[i])
            dfs(i+1)

            subset.pop()

            dfs(i+1)
        candidates.sort()
        dfs(0)
        return result
