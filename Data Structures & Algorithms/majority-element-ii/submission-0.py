class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        freq = defaultdict(int)
        for num in nums:
            if num in freq.keys():
                freq[num] +=1
            else:
                freq[num] =1
        for key,val in freq.items():
            if val > (len(nums)//3):
                res.append(key)
        return res