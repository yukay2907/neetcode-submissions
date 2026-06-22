class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n-2):

            l = i+1
            r = n-1
            req_sum = -nums[i]
            while l < r:
                cur_sum = nums[l]+nums[r]
                if cur_sum == req_sum:
                    result.append([nums[i],nums[l],nums[r]])
                if cur_sum < req_sum:
                    l+=1
                else:
                    r-=1

        a = []
        for i in result:
            if i not in a:
                a.append(i)
                
        return a