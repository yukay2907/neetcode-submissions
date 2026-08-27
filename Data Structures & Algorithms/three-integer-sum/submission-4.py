class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                total = nums[j] + nums[k]
                if total == target:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif total < target:
                    j += 1
                else:
                    k -= 1
        
        seen = set()
        ans = []
        for subarr in res:
            t = tuple(subarr)
            if t not in seen:
                seen.add(t)
                ans.append(subarr)
        return ans