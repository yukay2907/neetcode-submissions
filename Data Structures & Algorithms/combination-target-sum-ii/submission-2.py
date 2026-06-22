class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(ind,curr_set,remaining):
            if remaining == 0:
                result.append(curr_set.copy())
                return

            if remaining < 0:
                return

            for i in range(ind,len(candidates)):
                if i > ind and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > remaining:
                    break
                curr_set.append(candidates[i])
                dfs(i+1,curr_set,remaining-candidates[i])
                curr_set.pop()
        
        dfs(0,[],target)
        return result