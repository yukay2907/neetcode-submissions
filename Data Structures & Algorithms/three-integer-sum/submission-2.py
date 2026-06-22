class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i+1
            r = n-1
            req_sum = -nums[i]
            while l < r:
                cur_sum = nums[l]+nums[r]
                if cur_sum == req_sum:
                    result.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                if cur_sum < req_sum:
                    l+=1
                else:
                    r-=1
        return result