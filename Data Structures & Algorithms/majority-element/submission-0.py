class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dict1 = defaultdict(int)
        for num in nums:
            if num in dict1:
                dict1[num] +=1
            else:   dict1[num] = 1
        for key,val in dict1.items():
            if val > n//2:
                return key
        print(dict1)